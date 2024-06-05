const { SlashCommandBuilder } = require('discord.js');

module.exports = {
    data: new SlashCommandBuilder()
    .setName('help')
    .setDescription('Lists all available commands'),

    async execute(interaction) {
        try {
            msg = '';
            const globalCommands = await interaction.client.application.commands.fetch();
            globalCommands.forEach(command => {
                msg += `</${command.name}:${command.id}>\n${command.description}\n\n`;
            });

            await interaction.reply({
                content: `There are currrently ${interaction.client.commands.size} available commands: \n${msg}`,
                ephemeral: true,
            });
        } catch (error) {
            console.log(`[ERROR❌] with help.js\n${error}`);
        }
    }
};
