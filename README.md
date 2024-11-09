# Discord Bot Uygulaması | Discord Bot Application

Bu Python uygulaması, Discord sunucularında çeşitli komutlar ve olaylarla etkileşime geçmek üzere yapılandırılmış bir Discord botudur.

This Python application is a Discord bot configured to interact with various commands and events on Discord servers.

## Özellikler | Features

- Discord sunucularında belirli komutları algılayıp yanıt verir.
- `discord.ext.commands` modülünü kullanarak genişletilebilir bir komut yapısına sahiptir.
- Üye yönetimi ve mesajlara tepki verme gibi temel Discord bot işlevlerini içerir.

- Responds to specific commands in Discord servers.
- Uses the `discord.ext.commands` module for an extendable command structure.
- Provides basic functions like member management and message responses.

## Kurulum | Setup

### Gereksinimler | Requirements
1. **Python 3.7 veya üzeri** | Python 3.7 or later

2. **Gerekli Kütüphaneleri Yükleyin** | Install the Required Libraries:
    ```bash
    pip install discord.py
    ```

3. **Bot Token’ınızı Ekleyin** | Add Your Bot Token:
   - Discord geliştirici portalından bir bot oluşturun ve token alın.
   - `dc_bot.py` dosyasındaki `TOKEN` değişkenine botunuzun token'ını ekleyin.

   - Create a bot in the Discord Developer Portal and obtain a token.
   - Add your bot token to the `TOKEN` variable in `dc_bot.py`.

## Kullanım | Usage

Uygulamayı çalıştırmak için terminalde şu komutu kullanın:
Run the following command in the terminal to start the application:
```bash
python dc_bot.py
