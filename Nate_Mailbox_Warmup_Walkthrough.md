# Nate: connecting your mailbox and starting warmup

Steps verified against Clay's current sequencer docs (university.clay.com/docs/email-sequencer), Jul 10 2026. This is the only piece that has a clock on it, which is why it goes first. Everything else on the runway is mine. Should take you about 10 minutes.

## 1. Connect your mailbox

1. In Clay, from the home screen open **Campaigns**, then the **Email accounts** tab.
2. Click **Add email accounts** and pick **Microsoft Outlook OAuth** (we're on Microsoft; this is Clay's recommended path).
3. Sign in with your Intradiem account and approve the permissions it lists (send mail, read/write mail, mailbox settings; this is what lets it send as you and detect replies).

If you hit an access error at step 3, that means a Microsoft admin needs to authorize the Clay Sequencer app for our domain first. Stop there and tell me; I'll run down the approval. Don't retry it repeatedly.

## 2. Turn on warmup

1. Still in the **Email accounts** tab, find your account and **Enable warmup**.
2. Clay assigns the workspace a two-word keyphrase (something like `clever-rocket`) that marks every warmup email. Follow the in-app instructions to set up the label and filter so warmup traffic skips your inbox. With OAuth it sets most of this up automatically.
3. Leave warmup on permanently. Clay's own guidance is to keep it on at all times for any account in the sequencer.

## 3. Set the daily send limit low

In the same row, use **Update send limit** and set it low to start (I'd say 20 a day; that's our call, not Clay's). The limit only matters once we're live, but setting it now means nothing can ever spike volume from your account.

## 4. What happens next

The mailbox builds sending reputation for the next 2 to 3 weeks while I finish the list work on my side (customer exclusions, campaign cleanup, loading the drafts). Nothing sends from your account in that time except the automated warmup traffic, which goes to other warmup inboxes, never to prospects.

Two things worth knowing:

- If warmup switches itself off, that's Clay protecting your sender reputation because Microsoft throttled something. Don't turn it back on; just tell me and we'll figure out why.
- You don't need to touch the campaign itself. When the drafts are loaded you'll be able to read every email in the campaign's **Leads** tab before anything is ever approved to send, and the send button stays off until we've walked it together.
