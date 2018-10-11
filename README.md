# Chattervox Key Registry

A central key server for [chattervox](https://github.com/brannondorsey/chattervox) public keys. Add your key!

- View the [active keys](https://raw.githubusercontent.com/brannondorsey/chattervox-keys/master/active.tsv)
- View the [revoked keys](https://raw.githubusercontent.com/brannondorsey/chattervox-keys/master/revoked.tsv)

## Add Your Public Key

Keys are added to this list via pull requests.

### Getting your public key

A public key will be automatically created for you the first time you run [chattervox](https://github.com/brannondorsey/chattervox). Run `chattervox showkey` and look for a line like this:

```
KC3LZO Public Key (your signing key): 044da0d4c38bed6e5bc418231cb2dca4f690d858d36c38a032732553b76262a1adfccf588b6c1f9d7734b1bbce90914f82
```

This long hexadecimal number is your P192 public key. Copy it to your clipboard as we'll use it in the next step.

### Adding your key to this list

Fork and clone this repository. Create a new folder in `KEYS/` with an `active.txt` file containing your key. Make a pull request.

```bash
git clone https://github.com/YOUR_FORK/chattervox-keys
cd chattervox-keys

# make a new folder in KEYS/ using your callsign
mkdir KEYS/YOUR_CALLSIGN
cd KEYS/YOUR_CALLSIGN

# create active.txt and add your public key to this file. 
# You can add multiple keys, one per line.
touch active.txt
# ... add your public keys in active.txt

# if you have any keys that have been compromised or you would like to revoke
# you can create a revoke.txt file and add them in there
# touch revoke.txt
```

For an example, see [`KEYS/EXAMPLE/`](KEYS/EXAMPLE).

**DO NOT** edit the `active.tsv` or `revoked.tsv` files in the root folder. These lists are automatically generated to avoid merge conflicts and should not be touched. **ONLY** make PRs with additions and changes to files in your `KEYS/YOUR_CALLSIGN` folder. Once you've added or edited your folder, make a PR from your fork to the `master` branch of [brannondorsey/chattervox-keys](https://github.com/brannondorsey/chattervox-keys).

You can add whatever other files to your folder as you please, only `active.txt` and `revoked.txt` will be recognized by the automatic list compiler that creates the active and revoked lists. If you have any additional identity proofs you'd like to share with other chattervox users this folder is a great place to do so. For instance you could create a `README.md` file in your folder and introduce yourself, link to your entry in the FCC database, or sign your public key using a [Keybase](https://keybase.io/) signature. Your folder is your own space to do what you want.

## Thoughts

This repository sprung from a discussion on a [chattervox issue](https://github.com/brannondorsey/chattervox/issues/14). A public key server as a GitHub repository is unconventional but it was a quick solution that served the role. Down the road, we may use a different system if there is demand. This system has its pros and its cons:

- Pros
    - GitHub profiles can act as real-world identity proofs
    - Free public hosting on the web
    - GitHub API could be used to automatically fetch keys
    - Changes to a callsign's keys can be limited to the original submitter only
    - A human can vet the submitter's identity
    - Anyone can propose a key addition using a PR
- Cons
    - A central gatekeeper (repo owner or admins)
    - Keys can't be added without a GitHub account

I'm also hoping to add a system for users that know one another to verify each other's identities by signing each other's keys. I've got to add this standard message signature feature to chattervox first though. The idea is that in addition to the `active.txt` and `revoked.txt` files, a user could add a `signatures.tsv` with a list of callsigns whose public keys they've signed as a way to vouch for the validity of those callsigns and public keys.