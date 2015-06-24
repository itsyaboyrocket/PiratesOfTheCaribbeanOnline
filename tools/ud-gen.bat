@echo off

rem Args: If you want the entire directory to have UDs, then add --directory. Otherwise, add the name of the distributed class (without the UD included at the end).
rem For example, for directory, you could do: python ud-gen.py --directory
rem Otherwise, you could do: python ud-gen.py DistributedIsland

python ud-gen.py --directory
pause