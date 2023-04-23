# Run Bark on Lambda Labs

This script assumes you are running on a VM without any persistent filesystem. It’s a cold start that installs everything.

## Deploy and run

```sh
./deploy_and_run.sh <ip_address>
```

- copies run.py, prompts.txt and run.sh
- executes run.sh

Run will download:

- Bark repo
- Install dependencies
- Run generations

## More

Add to `prompts.txt` and run `more.sh` to get more generations:

```sh
./more.sh <ip_address>
```

## Export outputs

```sh
./export-outputs.sh <ip_address>
```

Run in the background to frequenty rsync any generations back to your local machine.

Will attempt to rsync every 10 seconds, will stop on error (like if the instance is terminated).
