# RandomNumber — Safe Bash and Git Experiment

Developer: Hamdy Abou El Anein
Contact: hamdy.aea@protonmail.com
License: GNU GPL v3 (see LICENSE).

Generate a random integer between 1 and 10. The historical version was
designed for a CentOS cron job, but contained hard-coded `/root` paths,
automatically pushed commits and **deleted its own README and output file**.

The modern script is portable and **does not change files or contact
GitHub by default**.

## Usage

```sh
./random.bsh                       # Preview only, no writes
./random.bsh --write               # Update random_Num if number >= 4
./random.bsh --publish             # Explicitly commit and push random_Num
./random.bsh --threshold 1 --write # Always write
```

`--publish` requires Git authentication to be configured securely and
a normal checked-out branch. It stages **only** `random_Num`, not the
entire directory, and never removes README or other files. Do not embed
passwords or access tokens in the script or cron entry.

For tests, `--number N` overrides randomness but is forbidden with
`--publish`. `--output FILE` can write a new file outside the checkout
without overwriting existing custom files.

## Offline tests

```sh
bash -n random.bsh
python3 -m unittest discover -s tests -v
```

All tests use temporary files. No Git push or cron configuration is
performed during testing.

The original implementation is preserved in branch `old`.

<!-- latest-cron-draw -->

## Latest Raspberry Pi draw

24922 · 2026-11-08T16:00:04+01:00
