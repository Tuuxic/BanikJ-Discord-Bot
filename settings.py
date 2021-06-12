import discord

# Bot
TOKEN = "ODQ4ODY2MTA5MjEwMDk5NzQz.YLS2Kw.InfAqkwFDL8HLdsMnSpDa6CHLl8"

# Admin
adminName = "Tuuxic"

# Default values
trigger = "$"
leakServer = 577069622105210900
defaultImgPATH = "C:\\Users\\prjan\\Pictures\\Bot"

# Selenium
driverPATH = "C:\\Program Files (x86)\\chromedriver.exe" 

# Functionality
imgDirPATH = "E:\\PCBackup\\Sachen\\Bilder\\Img"
synctubeLink = "https://sync-tube.de/create"
nhentaiLink = "https://nhentai.net/"

nhFindRx = r"nhentai find ([0-9]*)"
nhRandRx = r"nhentai random"

auditLogCategory = {
  discord.AuditLogActionCategory.create: "Create: ",
  discord.AuditLogActionCategory.update: "Update: ",
  discord.AuditLogActionCategory.delete: "Delete: ",
  None:                                  "Other:  "
}

actionType = {
  discord.AuditLogAction.channel_create:      "Create a channel",
  discord.AuditLogAction.channel_update:      "Update a channel",
  discord.AuditLogAction.channel_delete:      "Delete a channel",
  discord.AuditLogAction.overwrite_create:    "Create a overwrite",
  discord.AuditLogAction.overwrite_update:    "Update a overwrite",
  discord.AuditLogAction.overwrite_delete:    "Delete a overwrite",
  discord.AuditLogAction.kick:                "Kick a user",
  discord.AuditLogAction.member_prune:        "Prune a user",
  discord.AuditLogAction.ban:                 "Ban a user",
  discord.AuditLogAction.unban:               "Unban a user",
  discord.AuditLogAction.member_update:       "Update a user",
  discord.AuditLogAction.member_role_update:  "Update the role of a user",
  discord.AuditLogAction.member_move:         "Move a user",
  discord.AuditLogAction.member_disconnect:   "Disconnect a user",
  discord.AuditLogAction.bot_add:             "Add a bot",
  discord.AuditLogAction.role_create:         "Create a role",
  discord.AuditLogAction.role_update:         "Update a role",
  discord.AuditLogAction.role_delete:         "Delete a role",
  discord.AuditLogAction.invite_create:       "Create a invitation",
  discord.AuditLogAction.invite_update:       "Update a invitation",
  discord.AuditLogAction.invite_delete:       "Delete a invitation",
  discord.AuditLogAction.webhook_create:      "Create a webhook",
  discord.AuditLogAction.webhook_update:      "Update a webhook",
  discord.AuditLogAction.webhook_delete:      "Delete a webhook",
  discord.AuditLogAction.emoji_create:        "Create a emoji",
  discord.AuditLogAction.emoji_update:        "Update a emoji",
  discord.AuditLogAction.emoji_delete:        "Delete a emoji",
  discord.AuditLogAction.message_delete:      "Delete a message",
  discord.AuditLogAction.message_bulk_delete: "Bulk delete messages",
  discord.AuditLogAction.message_pin:         "Pin a message",
  discord.AuditLogAction.message_unpin:       "Unpin a message",
  discord.AuditLogAction.integration_create:  "Create an integration",
  discord.AuditLogAction.integration_update:  "Update an integration",
  discord.AuditLogAction.integration_delete:  "Deleta an integration",
  discord.AuditLogAction.guild_update:        "Update Server",
  None:                                       "Unknown action"
}

imgType = {
  "img": "Fanart",
  "meme": "Memes",
  "nsfw": "NSFW",
  "reaction": "ReactionImages"
}
