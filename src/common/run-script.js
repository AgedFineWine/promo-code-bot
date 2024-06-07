const util = require('util');
const exec = util.promisify(require('child_process').exec);

module.exports = async function(scriptPath) {
    try {
        const { stdout, stderr } = await exec(`python ${scriptPath}`);

        if (stderr) {
            console.log(stderr);
            return 'Some error occured.';
        }
        return stdout;
    } catch (error) {
        console.log(error);
        return 'Some error occured. Promise unfulfilled';
    }
};
