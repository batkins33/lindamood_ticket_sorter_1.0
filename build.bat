@echo off
echo Building Lindamood Ticket Sorter executable...
pyinstaller lindamood_sorter.spec --clean --noconfirm
echo Done. Check the /dist/LindamoodTicketSorter folder.
pause
