# DA2025_Lectures

1. Fork this repo 
2. Clone YOUR fork into your Marcy Lab folder (this should be in Documents or Desktop)

``` git clone https://github.com/YOUR_USERNAME/DA2025_Lectures.git ```

3. Navigate into the repo and add THIS repo as the upstream (this allows you to fetch changes from a parent repo)

``` git remote add upstream https://github.com/The-Marcy-Lab-School/DA2025_Lectures.git ```

## When there are new lectures or lecture notes to fetch down

4. Fetch those changes/new lectures 

```git fetch upstream```

5.  Merge the changes/new lectures into YOUR fork 

```git merge upstream/main -m "meaningful message```

6.  Push and changes you make to lectures/notes back to YOUR fork (these will be your personal notes/changes)

```git push origin main```