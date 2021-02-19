Electrum ABC is a fork of the open source Electron Cash wallet
(www.electroncash.org) for BCHA.

The Electrum ABC software is NOT affiliated, associated, or endorsed by
Electron Cash, electroncash.org, Electrum or electrum.org.


# Usage

When you first run Electrum ABC it will use a different configuration
directory to Electron Cash. On Unix it is ".electrum-abc", and on Windows/MacOS
it is "ElectrumABC".  Your wallet files will be copied from the Electron Cash
configuration directory if found.

Initially transactions will show up as unverified because
Electrum ABC is downloading the blockchain headers to verify the transactions.
This can take up to 10 minutes, but is only done once.

Ensure you are running Electrum ABC and not Electron Cash by checking for
"Electrum ABC" in the title bar wording.

We STRONGLY recommend you get comfortable and only send a small amount of BCHA
coins at first, to yourself, to confirm the network is processing your
transactions as expected.


# Miscellaneous

BCHA is a cryptocurrency that was created during the recent Bitcoin Cash chain
split. When a chain split happens, one chain will typically hold onto the
original cryptocurrency name and ticker, while the other chain will become
a separate cryptocurrency with new branding. In this case, BCHN held on to
the BCH name and ticker.

That means BCHA will soon be branded with an official coin name, logo, and
ticker. After it launches, there will likely be a new release of Electrum ABC
with a new name.

In the meantime you can find out more about BCHA here:
https://bitcoinabc.org/bcha/

# Release notes

## Release 4.3.0

 The first release is based on the
Electron Cash 4.2.0 codebase with the following changes

- updated list of electrum servers
- updated icons and branding
- use different directory for wallets and configuration
- automatically import wallets and some configuration files from Electron Cash


## Release 4.3.1

- Fixed a bug happening when clicking on a server in the network overview
  dialog.
- Enable the fiat display again, using CoinGecko's price for BCHA.
- Add a checkpoint to ensure only BCHA servers can be used. When splitting
  coins, it is now recommended to run both Electrum ABC and Electron Cash.
- Improve the automatic importing of wallets and user settings from
  Electron Cash, for new users: clear fiat historic exchange rates to avoid
  displaying BCH prices for pre-fork transactions, clear the server blacklist
  and whitelist, copy also testnet wallets and settings.
- When creating a new wallet, always save the file in the standard user
  directory. Previously, wallets were saved in the same directory as the
  most recently opened wallet.
- Change the crash report window to redirect users to github in their
  web browser, with a pre-filled issue ready to be submitted.
- Fix a bug when attempting to interact with a Trezor T hardware wallet
  with the autolock feature enabled, when the device is locked.


## Release 4.3.2

- Decrease the default transaction fee from 80 satoshis/byte to 10 sats/byte
- Add an option in the 'Pay to' context menu to scan the current screen
  for a QR code.
- Add a documentation page [Contributing to Electrum ABC](CONTRIBUTING.md).
- Remove the deprecated CashShuffle plugin.
- Specify a default server for CashFusion.
- Fix a bug introduced in 4.3.1 when starting the program from the source
  package when the `secp256k1` library is not available. This bug did not
  affect the released binary files.
- Fix a bug related to the initial automatic copy of wallets from the
  Electron Cash data directory on Windows. The configuration paths were not
  changed accordingly, causing new wallets to be automatically saved in the
  Electron Cash directory.


## Release 4.3.3

- Support restoring wallets from BIP39 word lists in other languages than
  english. New seeds phrases are still generated in english, because most
  other wallets only support english.
- Use the new derivation path `m/44'/899'/0` by default when creating or
  restoring a wallet. This is a pre-filled parameter that can be modified
  by the user. The BCH and BTC derivations paths are shown in a help
  message for users who wish to restore pre-fork wallets.
- Prefer sending confirmed coins when sending a transaction. Unconfirmed coins
  can still be used when necessary or when they are manually selected.
- Display a warning when sending funds to a legacy BTC address.
- Update some default configuration parameters the first time the user runs
  a new version of Electrum ABC (default fee, default CashFusion server).
- Display localized amounts with thousands separators to improve readability
  when switching the unit to mBCHA or bits.
- Always show the prefix when displaying a CashAddr in the user interface.
  This will prevent confusion when the prefix is changed, in the future.
- Support arbitrary CashAddr prefixes for the address conversion tool.
- Improvements to the Satochip plugin:
  - use BIP39 seeds by default instead of electrum seeds.
  - 2FA config is removed from initial setup, and can be activated from the
    option menu instead (clicking on the Satochip logo on the lower right
    corner).
  - PIN can have a maximum length of 16, not 64.
- Add a menu action in the Coins tab to export data for selected UTXOs to a
  JSON file.
- Use satoshis as a unit for amounts when generating payment URIs and QR codes.
  This aligns Electrum ABC with CashTab, Stamp and Cashew.
- Lower the default transaction fee from 10 satoshis/byte to 5 satoshis/byte.
- Minor performance improvements when freezing coins and saving wallet files.
