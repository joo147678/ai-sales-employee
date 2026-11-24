# Instagram for Agent 3: official Meta API (Business Discovery)

Free and official. It lets our Instagram account (builtbyjoo) read **public Business/Creator accounts** of other people: bio, website, followers, post count, and the last posts (caption, date, type, likes, comments, link). Personal (non-professional) accounts don't show up. In that case Agent 3 writes "not visible".

Decided by Mohamed on 2026-11-24 (instead of Apify or scrapers).

## Mohamed's setup (one time, ~20 minutes)

### 1. Check the Instagram account
- builtbyjoo must be a **Professional** account (Business or Creator).
- It must be **linked to a Facebook Page**: Instagram > Settings > Accounts Center, or from the Page settings > Linked accounts.

### 2. Create a Meta app (done 2026-11-25: app "builtbyjoo sales", ID 1188355310435502, portfolio مُحَمَّد يُوسُف, use cases Instagram + Pages; permissions added: instagram_basic, instagram_manage_insights, pages_read_engagement, pages_show_list, business_management. Don't use "my content ecosystem": Mohamed uses it for something else)
1. Open https://developers.facebook.com/apps and choose **Create App**.
2. Pick the type **Business**, or "Other" then Business. Give it a name like `builtbyjoo sales`.
3. In the app, add the **Instagram** product, choosing "API setup with Facebook login" (Instagram Graph API).
4. Leave the app in **Development** mode. It works for you as the app admin, and no app review is needed.

### 3. Get a token
1. Open https://developers.facebook.com/tools/explorer
2. Pick your app at the top right.
3. **Add permissions:** `instagram_basic`, `instagram_manage_insights`, `pages_show_list`, `pages_read_engagement`, `business_management`.
4. Click **Generate Access Token** and approve with your Facebook account. Choose the Page linked to Instagram.
5. The token only lasts an hour. To make it last 60 days, open https://developers.facebook.com/tools/debug/accesstoken, paste the token, then click **Extend Access Token**.

### 4. Get the Instagram User ID
In Graph API Explorer, run:
`me/accounts?fields=name,instagram_business_account`
Take the `id` under `instagram_business_account`. It's a long number starting with 1784...

### 5. Put them in the cloud environment (not in the chat and not in GitHub)
1. Open claude.ai/code and go to the environments.
2. Open **sales web**, then Edit, then **Environment variables**.
3. Add:
   - `META_IG_TOKEN` = the 60-day token
   - `IG_USER_ID` = the number from step 4
4. Click **Save**, then tell Claude "added".

> The token is a secret: never paste it into the chat or into any file in the repo.
> It expires after 60 days. When it does, the Pipeline sends an alert ("Instagram token expired") and you repeat step 3 and update the variable. A permanent token can come later through a System User in Business Settings.

## How the agents use it
```
curl -sg "https://graph.facebook.com/v21.0/$IG_USER_ID?fields=business_discovery.username(HANDLE){username,name,biography,website,followers_count,media_count,media.limit(12){caption,timestamp,media_type,like_count,comments_count,permalink}}&access_token=$META_IG_TOKEN"
```
- Error 110/100 "Invalid user id" or nothing returned = personal account or the handle doesn't exist, so "not visible".
- Error 190 = the token expired, so one alert to Mohamed.
- Limit: ~200 calls per hour. The Pipeline uses at most 30 per run.
- Use `curl -g` (otherwise curl treats {} in the URL as a glob and the response breaks).
- Read only. The API can't follow, like or DM anyone.
