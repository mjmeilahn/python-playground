"""
TO ADD LAYER(S) IN LAMBDA:
1. Create Simple Folder e.g. mkdir requests (from pip install requests)
2. cd requests
3. Install individual packages:
   pip install requests -t python/lib/python3.10/site-packages
4. Go into the /requests folder. The /python folder should be a child.
5. Zip the folder e.g. zip -r python.zip python
6. Create Layer; Upload zipped file; Set correct run-time and architecture.
7. Include Layer in Function and set the correct version number.
8. Any manual layer uploads beyond here require a manual version number adjustment in the function.
"""
