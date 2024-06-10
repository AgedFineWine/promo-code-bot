const { SlashCommandBuilder } = require('discord.js');
const runPythonScript = require('../common/run-script.js');
const path = require('path');

const pythonScriptPath = path.join(__dirname, '..', 'python-scripts', 'mtg_codes.py');

module.exports = {
    data: new SlashCommandBuilder()
    .setName('mtgcodes')
    .setDescription('Replies with the latest Magic: The Gathering codes'),
    cooldownDuration: 60,

    async execute(interaction) {
        const msg = await runPythonScript(pythonScriptPath);
        await interaction.reply(msg);
    }
};
