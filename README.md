# Nordic Museum Depics

## Toolforge setup

Source code resides in `~/www/python/src/`,
a virtual environment is set up in `~/www/python/venv/`,
logs end up in `~/uwsgi.log`.

If the web service is not running for some reason, run the following command:
```
webservice --backend=kubernetes python3.5 start
```
If it’s acting up, try the same command with `restart` instead of `start`.

To update the service, run the following commands after becoming the tool account:
```
webservice --backend=kubernetes python3.5 shell
source ~/www/python/venv/bin/activate
cd ~/www/python/src
git fetch
git diff @ @{u} # inspect changes
git merge --ff-only @{u}
pip3 install -r requirements.txt
webservice --backend=kubernetes python3.5 restart
```

## License

The code in this repository is released under the MIT, as provided in the `LICENSE` file.
