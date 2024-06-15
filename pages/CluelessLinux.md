---
title: Linux Helpers
desc: Some small tutorials for Clueless trying to use Linux.
keywords: [Linux]
---

## Before anything

Before you troubleshoot, it is worth it to update and restart your system,
especially if you haven't updated in a while:

```bash
apt update
sudo apt upgrade
```

## Running `.exe` fails with program error

1. Open the directory containing the `.exe` in your terminal:
    a. Right click in file manager and click `Open in Terminal`
    b. Open Terminal and manually navigate to it
2. Ensure the file has the executable bit set:
    ```bash
    chmod +x ./<file>.exe
    ```
3. Try running the file directly:
    ```bash
    ./<file>.exe
    ```
4. Try running it through `wine`:
    ```bash
    wine ./<file>.exe
    ```

## Last resort

Try [googling][Google] your problem. Some issues may be too difficult to fix, so
lower your expectations. Some issues also have a tendency to disappear after a
few updates.

[Google]: https://google.com
