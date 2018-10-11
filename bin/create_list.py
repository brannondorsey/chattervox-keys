import os
import csv

def main():

    dirname = os.path.dirname(os.path.realpath(__file__))
    key_dir = os.path.realpath(os.path.join(dirname, '..', 'KEYS'))
    active_path  = os.path.realpath(os.path.join(dirname, '..', 'active.tsv'))
    revoked_path = os.path.realpath(os.path.join(dirname, '..', 'revoked.tsv'))

    if os.path.exists(active_path):
        os.unlink(active_path)

    if os.path.exists(active_path):
        os.unlink(active_path)

    callsigns = filter(lambda call:
                            os.path.isdir(os.path.join(key_dir, call)) 
                            and call not in [ 'EXAMPLE' ], 
                        os.listdir(key_dir))

    active_keys = dict()
    revoked_keys = dict()
    for call in callsigns:
        active  = os.path.join(key_dir, call, 'active.txt')
        revoked = os.path.join(key_dir, call, 'revoked.txt')
        active_keys[call]  = list(set(get_keys_from_file(active)))
        revoked_keys[call] = list(set(get_keys_from_file(revoked)))

    write_keys_to_csv(active_path, active_keys)
    write_keys_to_csv(revoked_path, revoked_keys)

def get_keys_from_file(path):
    if os.path.exists(path):
        with open(path, 'r') as f:
            return  [key.strip() for key in f.read().split('\n') if len(key) > 1 ]

def write_keys_to_csv(path, keys):
    with open(path, 'w') as f:
        writer = csv.writer(f, delimiter='\t',
                               quotechar='"', 
                               quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['callsign', 'public_key'])
        for call in sorted(keys.keys()):
            for key in keys[call]:
                writer.writerow([call, key])

if __name__ == '__main__':
    main()
