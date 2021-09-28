# YesCloud
Cloud. Reimagined.

Because old mistakes happen. And we will fix it. The right way:tm:.

This repo will replace [NoCloud](https://github.com/chong601/NoCloud) as the code there is beyond saving.

# So, why the need for new repo? Why not just replace the existing code instead?

Let's just say that I just don't wanna look at the old code too much.

There are a ton of issues stemming from inadequate planning and scope creep that made the project very annoying to work with.

## Folder Structure
All projects will live in `yescloud`, where it will be broken down into sub-sections:
- `api`

  `api` will contain YesCloud REST API that can be consumed by either a third-party implementation or by YesCloud web manager
- `cli`
  
  `cli` will contain YesCloud command-line tools to enhance the features that cannot be provided by YesCloud itself
- `core`

  `core` will contain YesCloud library that will be shared by `api`, `cli` and `web`
- `extras`
  
  `extras` will contain extra tools that will be used for situational cases
- `web`

  `web` contains the code to provide services to YesCloud web-based manager

## Repository Structure
`main` will be the place for the full working implementation of the entire platform when it's ready.

`develop` branch contains the current snapshot of the code snippets and prototypes that will be used.

Code in `main` branch will be released under MIT License when it's ready.

Code in `develop` branch will remain unlicensed (means all rights are reserved to me) until it's considered stable for use.

## WARNING
The code in develop is very untested and will screw up your system if you don't understand what they do. While the code is unlicensed, I will not pursue those that fork my project and take it down. Use the code at your own risk. Here be dragons!

## Acknowledgements
New logo coming soon!

## Shoutouts
[Homelab Discord](https://discord.gg/homelab) and [r/Homelab](https://www.reddit.com/r/homelab) subreddit users for their feedbacks.
