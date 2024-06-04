const { Events } = require('discord.js');

module.exports = {
    eventName: Events.ClientReady,

    async execute(clientReady) {
        console.log(`[SUCCESS ✅] Logged in as ${clientReady.user.username}!`);
    }
};
