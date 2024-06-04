const { SlashCommandBuilder } = require('discord.js');
const runPythonScript = require('../common/run-script.js');
const path = require('path');

const pythonScriptPath = path.join(__dirname, '..', 'python-scripts', 'genshin_codes.py');

module.exports = {
    data: new SlashCommandBuilder()
    .setName('genshincodes')
    .setDescription('Replies with the latest Genshin Impact codes'),

    async execute(interaction) {
        const msg = await runPythonScript(pythonScriptPath);
        await interaction.reply(msg);
    }
};
