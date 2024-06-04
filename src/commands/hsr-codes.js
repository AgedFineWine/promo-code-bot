const { SlashCommandBuilder } = require('discord.js');
const runPythonScript = require('../common/run-script.js');
const path = require('path');

const pythonScriptPath = path.join(__dirname, '..', 'python-scripts', 'hsr_codes.py');
console.log('ScriptPath::::' + pythonScriptPath);
module.exports = {
    data: new SlashCommandBuilder()
    .setName('hsrcodes')
    .setDescription('Replies with the latest Honkai Star Rail codes'),

    async execute(interaction) {
        const msg = await runPythonScript(pythonScriptPath);
        await interaction.reply(msg);
    }
};
