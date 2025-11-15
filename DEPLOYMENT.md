# Deploying to GitHub Pages

## Step 1: Create GitHub Repository

1. Go to [github.com](https://github.com) and create a new repository
2. Name it whatever you want (e.g., `goose-or-geese`)
3. Do NOT initialize with README, .gitignore, or license (we already have these)

## Step 2: Push Code to GitHub

Run these commands in your terminal:

```bash
cd /private/tmp/goose-or-geese
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin main
```

Replace `YOUR_USERNAME` and `YOUR_REPO_NAME` with your actual GitHub username and repository name.

## Step 3: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** (top right of the repo page)
3. Scroll down and click **Pages** in the left sidebar
4. Under **Source**, select the `main` branch
5. Leave the folder as `/ (root)`
6. Click **Save**

GitHub will provide a URL like `https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/`

## Step 4: Connect Custom Domain (gooseorgeese.com)

1. In the **GitHub Pages** settings, scroll to **Custom domain**
2. Enter `gooseorgeese.com` and click **Save**
3. GitHub will create a `CNAME` file in your repo

### DNS Configuration

In your domain registrar (where you bought gooseorgeese.com):

**Option A: Using CNAME (Recommended)**
- Add a CNAME record:
  - Name/Host: `www`
  - Value: `YOUR_USERNAME.github.io`
- Add an A record (for apex domain):
  - Name/Host: `@` or blank
  - Values (add all four):
    - `185.199.108.153`
    - `185.199.109.153`
    - `185.199.110.153`
    - `185.199.111.153`

**Option B: Using only CNAME**
- If your registrar supports CNAME flattening/ALIAS records:
  - Name/Host: `@` or blank
  - Value: `YOUR_USERNAME.github.io`

### Enable HTTPS

1. Wait 10-20 minutes for DNS to propagate
2. Go back to GitHub Pages settings
3. Check the box for **Enforce HTTPS**

Your site will be live at `https://gooseorgeese.com`!

## Updating the Site

Whenever you make changes:

```bash
git add .
git commit -m "Description of changes"
git push
```

GitHub Pages will automatically rebuild and deploy within 1-2 minutes.
