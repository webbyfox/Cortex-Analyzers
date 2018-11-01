from .constants import TLIPA_API

from cortexutils.analyzer import Analyzer


class TLIPA(Analyzer):

    def run(self):
        Analyzer.run(self)

        if self.data_type == 'ip':
            try:
                data = self.get_data()
               #Todo: Query TLIPA API to get result and generate json

            except ValueError as e:
                self.error('Invalid IP address')
            except AddressNotFoundError as e:
                self.error('Unknown IP address')
            except Exception as e:
                self.unexpectedError(type(e))
        else:
            self.notSupported()

if __name__ == '__main__':
    TLIPA().run()
