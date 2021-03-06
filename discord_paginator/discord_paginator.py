import discord
from discord import Message,Embed, ChannelType
from discord_slash.model import ButtonStyle
from discord_slash.utils.manage_components import create_button, create_actionrow,create_select, create_select_option,wait_for_component
from discord_slash import SlashCommand
from discord.ext.commands import Bot
import asyncio
from discord_slash.context import ComponentContext
from typing import Union,Optional, List

class Page:
    def __init__(self,
                 sendable : Union[SlashCommand,Message,ChannelType],
                 bot : Bot,
                 embeds : Optional[List[Embed]] = [],
                 content : Optional[List[str]] = [],
                 timeout : Optional[int] = None,
                 hidden : Optional[bool] = False,
                 skipper : Optional[bool] = False,
                 reply : Optional[bool] = False,
                 mention_author : Optional[bool] = False):
        self.sendable=sendable
        self.bot=bot
        self.embeds=embeds
        self.content=content
        self.timeout=timeout
        self.hidden=hidden
        self.skipper=skipper
        self.reply=reply
        self.mention_author=mention_author
        if len(self.embeds)>len(self.content):
            self.length=len(self.embeds)
            while not len(self.embeds)==len(self.content):
                self.content.append(None)
        elif len(self.embeds)<len(self.content):
            self.length=len(self.content)
            while not len(self.embeds)==len(self.content):
                self.embeds.append(None)
        else:
            self.length=len(self.content)
    async def send(self):
        self.count=1
        if type(self.sendable)==SlashCommand:
            if self.count==1 and self.count==self.length:
                self.components=[create_actionrow(create_button(label="Back",style=ButtonStyle.gray,custom_id="Back",disabled=True),
                                                create_button(label="Page "+str(self.count)+"/"+str(self.length),disabled=True,style=ButtonStyle.gray),
                                                create_button(label="Next",custom_id="Next",style=ButtonStyle.gray,disabled=True))]
                if self.skipper == True:
                    options=[]
                    u=1
                    while u < self.length+1:
                        options.append(create_select_option("Page "+str(u)+"/"+str(self.length),value=str(u))) 
                        u=u+1
                    self.components.append(create_actionrow(create_select(options=options,placeholder="Skip page",min_values=1,max_values=1,disabled=True)))
                msg = await self.sendable.channel.send(content=self.content[self.count-1],embed=self.embeds[self.count-1],components=self.components)
                return None
            else:
                self.components=[create_actionrow(create_button(label="Back",style=ButtonStyle.gray,custom_id="Back",disabled=True),
                                                create_button(label="Page "+str(self.count)+"/"+str(self.length),disabled=True,style=ButtonStyle.gray),
                                                create_button(label="Next",custom_id="Next",style=ButtonStyle.gray))]
                if self.skipper == True:
                    options=[]
                    u=1
                    while u < self.length+1:
                        options.append(create_select_option("Page "+str(u)+"/"+str(self.length),value=str(u))) 
                        u=u+1
                    self.components.append(create_actionrow(create_select(options=options,placeholder="Skip page",min_values=1,max_values=1)))
                msg = await self.sendable.channel.send(content=self.content[self.count-1],embed=self.embeds[self.count-1],components=self.components)
        elif type(self.sendable)==Message:
            if self.count==1 and self.count==self.length:
                self.components=[create_actionrow(create_button(label="Back",style=ButtonStyle.gray,custom_id="Back",disabled=True),
                                                create_button(label="Page "+str(self.count)+"/"+str(self.length),disabled=True,style=ButtonStyle.gray),
                                                create_button(label="Next",custom_id="Next",style=ButtonStyle.gray,disabled=True))]
                if self.skipper == True:
                    options=[]
                    u=1
                    while u < self.length+1:
                        options.append(create_select_option("Page "+str(u)+"/"+str(self.length),value=str(u))) 
                        u=u+1
                    self.components.append(create_actionrow(create_select(options=options,placeholder="Skip page",min_values=1,max_values=1,disabled=True)))
                if self.reply==True:
                    msg = await self.sendable.reply(content=self.content[self.count-1],embed=self.embeds[self.count-1],components=self.components,mention_author=self.mention_author)
                else:
                    msg = await self.sendable.channel.send(content=self.content[self.count-1],embed=self.embeds[self.count-1],components=self.components)
                return None
            else:
                self.components=[create_actionrow(create_button(label="Back",style=ButtonStyle.gray,custom_id="Back",disabled=True),
                                                create_button(label="Page "+str(self.count)+"/"+str(self.length),disabled=True,style=ButtonStyle.gray),
                                                create_button(label="Next",custom_id="Next",style=ButtonStyle.gray))]
                if self.skipper == True:
                    options=[]
                    u=1
                    while u < self.length+1:
                        options.append(create_select_option("Page "+str(u)+"/"+str(self.length),value=str(u))) 
                        u=u+1
                    self.components.append(create_actionrow(create_select(options=options,placeholder="Skip page",min_values=1,max_values=1)))
                if self.reply==True:
                    msg = await self.sendable.reply(content=self.content[self.count-1],embed=self.embeds[self.count-1],components=self.components,mention_author=self.mention_author)
                else:
                    msg = await self.sendable.channel.send(content=self.content[self.count-1],embed=self.embeds[self.count-1],components=self.components)
        elif type(self.sendable)==ChannelType:
            if self.count==1 and self.count==self.length:
                self.components=[create_actionrow(create_button(label="Back",style=ButtonStyle.gray,custom_id="Back",disabled=True),
                                                create_button(label="Page "+str(self.count)+"/"+str(self.length),disabled=True,style=ButtonStyle.gray),
                                                create_button(label="Next",custom_id="Next",style=ButtonStyle.gray,disabled=True))]
                if self.skipper == True:
                    options=[]
                    u=1
                    while u < self.length+1:
                        options.append(create_select_option("Page "+str(u)+"/"+str(self.length),value=str(u))) 
                        u=u+1
                    self.components.append(create_actionrow(create_select(options=options,placeholder="Skip page",min_values=1,max_values=1,disabled=True)))
                msg = await self.sendable.send(content=self.content[self.count-1],embed=self.embeds[self.count-1],components=self.components)
                return None
            else:
                self.components=[create_actionrow(create_button(label="Back",style=ButtonStyle.gray,custom_id="Back",disabled=True),
                                                create_button(label="Page "+str(self.count)+"/"+str(self.length),disabled=True,style=ButtonStyle.gray),
                                                create_button(label="Next",custom_id="Next",style=ButtonStyle.gray))]
                if self.skipper == True:
                    options=[]
                    u=1
                    while u < self.length+1:
                        options.append(create_select_option("Page "+str(u)+"/"+str(self.length),value=str(u))) 
                        u=u+1
                    self.components.append(create_actionrow(create_select(options=options,placeholder="Skip page",min_values=1,max_values=1)))
                msg = await self.sendable.send(content=self.content[self.count-1],embed=self.embeds[self.count-1],components=self.components)
        if type(self.sendable) in [SlashCommand,ChannelType,Message]:
            while True:
                try:
                    button_ctx : ComponentContext = await wait_for_component(client=self.bot,messages=msg,components=self.components,timeout=self.timeout)
                    if button_ctx.custom_id=="Next":
                        self.count=self.count+1
                    elif button_ctx.custom_id=="Back":
                        self.count=self.count-1
                    else:
                        self.count=int(button_ctx.values[0])
                    if self.count==1:
                        self.components = [create_actionrow(create_button(label="Back",style=ButtonStyle.gray,custom_id="Back",disabled=True),
                                                      create_button(label="Page "+str(self.count)+"/"+str(self.length),disabled=True,style=ButtonStyle.gray),
                                                      create_button(label="Next",custom_id="Next",style=ButtonStyle.gray))]
                        if self.skipper==True:
                            self.components.append(create_actionrow(create_select(options=options,placeholder="Skip page",min_values=1,max_values=1)))
                    elif self.count==self.length:
                        self.components = [create_actionrow(create_button(label="Back",style=ButtonStyle.gray,custom_id="Back"),
                                                      create_button(label="Page "+str(self.count)+"/"+str(self.length),disabled=True,style=ButtonStyle.gray),
                                                      create_button(label="Next",custom_id="Next",style=ButtonStyle.gray,disabled=True))]
                        if self.skipper==True:
                            self.components.append(create_actionrow(create_select(options=options,placeholder="Skip page",min_values=1,max_values=1)))
                    else:
                        self.components = [create_actionrow(create_button(label="Back",style=ButtonStyle.gray,custom_id="Back"),
                                                          create_button(label="Page "+str(self.count)+"/"+str(self.length),disabled=True,style=ButtonStyle.gray),
                                                          create_button(label="Next",custom_id="Next",style=ButtonStyle.gray))]
                        if self.skipper==True:
                            self.components.append(create_actionrow(create_select(options=options,placeholder="Skip page",min_values=1,max_values=1)))
                    await button_ctx.edit_origin(content=self.content[self.count-1],embed=self.embeds[self.count-1],components=self.components)
                except:
                    self.components = [create_actionrow(create_button(label="Back",style=ButtonStyle.gray,custom_id="Back",disabled=True),
                                                          create_button(label="Page "+str(self.count)+"/"+str(self.length),disabled=True,style=ButtonStyle.gray),
                                                          create_button(label="Next",custom_id="Next",style=ButtonStyle.gray,disabled=True))]
                    if self.skipper==True:
                        self.components.append(create_actionrow(create_select(options=options,placeholder="Skip page",min_values=1,max_values=1,disabled=True)))
                    await msg.edit(components=self.components)
                    break
