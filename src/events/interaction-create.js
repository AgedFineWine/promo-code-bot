const { Collection, Events } = require('discord.js');

module.exports = {
    eventName: Events.InteractionCreate,

    async execute(interaction) {
        if (!interaction.isChatInputCommand()) return;
        if (!interaction.client.commands.has(interaction.commandName)) {
            console.log(`${interaction.commandName} was not found in the collection`);
            return;
        }

        const command = interaction.client.commands.get(interaction.commandName);
        const cooldowns = interaction.client.cooldowns;
        const userId = interaction.user.id;
        
        if ('cooldownDuration' in command) {
            if (!cooldowns.has(command.data.name)) {
                cooldowns.set(command.data.name, new Collection());
            }

            const currentTime = Date.now();
            const timestamp = cooldowns.get(command.data.name);

            const cooldownAmount = command.cooldownDuration * 1000;

            if (timestamp.has(userId)) {
                const expirationTime = timestamp.get(userId) + cooldownAmount;
                if (currentTime < expirationTime) {
                    const timeDifference = Math.round(Math.floor((1 / 1000) * (expirationTime - currentTime)));

                    return interaction.reply({
                        content: `You are currently on cooldown for </${interaction.commandName}:${interaction.commandId}>. You may use this command again after ${timeDifference} seconds.`,
                        ephemeral: true,
                    });
                }
            }
            
            timestamp.set(userId, currentTime);
            setTimeout(() => {
                return timestamp.delete(userId);
            }, cooldownAmount);
        }

        try {
            await command.execute(interaction);
        } catch (error) {
            console.log(error);
        }
    }
};
