import asyncio
import alien_invasion  # imports module; run() is defined at module level in alien_invasion.py

async def main():
    # Call the module-level run() so the normal game loop starts.
    # When called from pygbag, we keep the asyncio loop alive afterwards.
    alien_invasion.run()
    while True:
        await asyncio.sleep(0)

asyncio.run(main())
