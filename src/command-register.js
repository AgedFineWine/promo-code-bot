require('dotenv').config();
const { REST, Routes } = require("discord.js");
const path = require('path');
const fs = require('fs');

const commandsArray = [];

const commandFolderPath = path.join(__dirname, 'commands');
const commandFolderFiles = fs.readdirSync(commandFolderPath).filter(file => file.endsWith('.js'));

for (const file of commandFolderFiles) {
    const filePath = path.join(commandFolderPath, file);
    const command = require(filePath);

    if ('data' in command && 'execute' in command) {
        commandsArray.push(command.data.toJSON());
    } else {
        console.log(`Something went wrong with appending a command to the commands list.
         Source of error: ${filePath}`);
    }
}

const rest = new REST({ version: '10' }).setToken(process.env.BOT_TOKEN);

async function registerCommands() {
    try {
        console.log(`[Loading⏳] Started refreshing  ${commandsArray.length} application (/) commands.`);

		const data = await rest.put(
			Routes.applicationCommands(process.env.CLIENT_ID),
			{ body: commandsArray },
		);

        console.log(`[SUCCESS✅] Loaded ${data.length} application (/) commands.`);
    } catch (error) {
        console.log(error);
    }
}

registerCommands();
