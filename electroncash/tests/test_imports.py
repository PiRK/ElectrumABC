
import unittest


class TestImportModules(unittest.TestCase):
    """Very basic test to check that all modules can be successfully imported.
    This can prevent some obvious regressions (names not defined,
    import errors...)

    I will not cover any code inside functions or methods, only code
    that is executed at import time.
    """
    def test_import_modules(self):
        try:
            from .. import (
                address,
                asert_daa,
                base_wizard,
                bitcoin,
                blockchain,
                caches,
                cashacct,
                coinchooser,
                commands,
                constants,
                contacts,
                daemon,
                dnssec,
                ecc_fast,
                exchange_rate,
                i18n,
                interface,
                jsonrpc,
                keystore,
                migrate_data,
                mnemonic,
                msqr,
                old_contacts,
                old_mnemonic,
                paymentrequest,
                paymentrequest_pb2,
                pem,
                plugins,
                ripemd,
                rsakey,
                schnorr,
                secp256k1,
                simple_config,
                storage,
                transaction,
                util,
                verifier,
                version,
                wallet,
                web,
                winconsole,
                x509
            )
        except Exception as e:
            self.fail((str(e)))

    def test_import_optional_dependencies(self):
        """Some modules can only be imported if a specific dependency
        is available"""
        # websockets is required if the command line
        try:
            from SimpleWebSocketServer import WebSocket, SimpleSSLWebSocketServer
        except ImportError:
            pass
        else:
            try:
                from .. import websockets
            except Exception as e:
                self.fail(str(e))


if __name__ == '__main__':
    unittest.main()
