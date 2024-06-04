const { Collection, Events, time, TimestampStyles} = require('discord.js');
const path = require('path');
const fs = require('fs');

module.exports = {
    eventName: Events.InteractionCreate,

    async execute(interaction) {
        if (!interaction.isChatInputCommand()) return;
        if (!interaction.client.commands.has(interaction.commandName)) {
            console.log(`${interaction.commandName} was not found in the collection`);
            return;
        }

        const command = interaction.client.commands.get(interaction.commandName);

        try {
            await command.execute(interaction);
        } catch (error) {
            console.log(error);
        }
    }
};
