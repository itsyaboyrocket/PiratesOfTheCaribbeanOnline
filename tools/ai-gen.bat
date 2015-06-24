@echo off

rem Args: If you want the entire directory to have AIs, then add --directory. Otherwise, add the name of the distributed class (without the AI included at the end).
rem For example, for directory, you could do: python ai-gen.py --directory
rem Otherwise, you could do: python ai-gen.py DistributedIsland

python ai-gen.py --directory
pause