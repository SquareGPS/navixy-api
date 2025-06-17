---
description: Instructions to add localizations for Navixy Platform
---
# Translate Navixy

Navixy is dedicated to global accessibility, offering support for a [wide range of languages](https://docs.navixy.com/admin-panel/regional-settings#languages) to cater to users worldwide. The platform is designed to be versatile, accommodating both left-to-right and right-to-left languages. We continually expand our language support through contributions from our vibrant community of translators. If the language you need isn't yet supported, we invite you to join us and help expand our multilingual capabilities.

## Currently Supported Languages

Navixy currently supports dozens of languages, with more being added regularly. For the most up-to-date list of supported languages, visit our [regional settings documentation](https://docs.navixy.com/admin-panel/regional-settings#languages).

## How to Become a Contributor

We welcome and appreciate all contributions. By joining our community of translators, you help make Navixy more accessible and user-friendly for people around the world. Start translating today and become part of a global effort to enhance the Navixy platform.

### Step 1: Get Access to Crowdin

To start contributing, you will need access to our Crowdin project. [Crowdin](https://crowdin.com/ "https://crowdin.com/") is an online translation service developed specifically for team-based translation projects. Contact your Navixy representative and provide your Crowdin account details to be associated with the Navixy Crowdin project.

### Step 2: Choose Your Translation Method

There are two primary methods to localize the Navixy platform:

1. **Crowdin In-context Translation (Web UI Only)**
    
2. **Crowdin UI Translation**
    

#### Crowdin In-context Translation (Web UI Only)

This method is the most convenient way to translate the Navixy Web UI. Use the following link to launch the Crowdin In-context service:

`<https://demo.navixy.com/?locale=ach#/login>`

After logging in, the standard Navixy UI will appear in a special translation mode. Click on the small icon next to each text item to open the translation dialog and make your edits.

#### Crowdin UI Translation

For a more comprehensive translation experience, use the Crowdin UI. This method is essential for translating backend components and mobile apps. Translations in Crowdin are organized into several directories:

1. **Common Server properties, API server properties, Tracking server properties, SMS server properties**: Translation strings for backend (mainly for reports, SMS, and email notifications).
    
2. **Future Web UI, Legacy Web UI**: Translation strings for Navixy Web UI.
    
3. **android-client, android-tracker, navixy-tracker-ios, navixy-viewer-ios**: Translation strings for mobile apps.
    

Each directory contains specific strings for translation, which you can edit directly in the Crowdin interface.

## Contributing to New or Existing Languages

### Adding a New Language

If you want to add a new language:

1. Obtain a Crowdin account by contacting your manager.
    
2. Use either the In-context translation method or the Crowdin UI to start translating.
    
3. Notify your manager once the translation is complete. The development team will then add the new language to the platform.
    

### Improving Existing Translations

To improve existing translations, follow the same steps as above, but focus on refining and enhancing the current language packs. Your contributions will be reviewed and, once approved, will be automatically deployed to the production environment.

## Translation Delivery

Deploying translations to the production environment typically takes about a week. For on-premise installations and mobile apps, this timing depends on their respective release schedules. Once your translation work is complete, notify your Navixy representative to ensure your contributions are integrated into the platform.