require('dotenv').config();
const { Client, Collection, GatewayIntentBits } = require('discord.js');
const path = require('path');
const fs = require('fs');

const client = new Client({
    intents: [
        GatewayIntentBits.Guilds,
        GatewayIntentBits.GuildMessages,
    ],
});

client.cooldowns = new Collection(); // key: command Name -> value: new Collection -> key: userID -> value: current time
client.commands = new Collection(); // key: command Name -> value: entire command object

const commandsFolderPath = path.join(__dirname, 'commands');
const commandsFolder = fs.readdirSync(commandsFolderPath);

for (const file of commandsFolder) {
    const commandsFilePath = path.join(commandsFolderPath, file);
    const commandFile = require(commandsFilePath);

    if ('data' in commandFile && 'execute' in commandFile) {
        client.commands.set(commandFile.data.name, commandFile);
    } else {
        console.log(`[ERROR❌] ${commandsFilePath} is missing either or both of the "data" and "execute" attribute.`);
    }
}

// the section below handles the events the bot is listening to

const eventsFolderPath = path.join(__dirname, 'events');
const eventsFolder = fs.readdirSync(eventsFolderPath);

for (const file of eventsFolder) {
    const filePath = path.join(eventsFolderPath, file);
    const eventFile = require(filePath);

    if ('eventName' in eventFile && 'execute' in eventFile) {
        client.on(eventFile.eventName, (...args) => eventFile.execute(...args)); // experiment without callback function?
    }
}

client.login(process.env.BOT_TOKEN);
