class Configuration:
  """
  Holds and provides access to library configuration.
  """

  _instance = None

  def __new__(cls):
    """
    Creates a new instance only if one doesn't already exist.
    """
    if cls._instance is None:
      cls._instance = super().__new__(cls)
      cls._instance._config = {}  # Private dictionary for configuration
    return cls._instance

  def __init__(self):
    self._config = {}  # Private dictionary for configuration

  def set_config(self, clientId, merchantId, privateKeyPath, environment):
    """
    Sets the configuration values.

    @params:
        - clientId: Your client ID.
        - merchantId: Your merchant ID.
        - privateKeyPath: Path to your private key file.
        - environment: The environment (production, sandbox, test4).
    """
    self._config = {
        'VODAPAY_CLIENT_ID': clientId,
        'VODAPAY_MERCHANT_ID': merchantId,
        'PRIVATE_KEY_PATH': privateKeyPath,
    }
    self._config.update(self.set_environment(environment))  # Update with environment

  def set_environment(self, environment):
    if environment.lower() in environments:
        return {'VODAPAY_BASEURL': environments[environment]}
    else:
        raise ValueError(f'Invalid environment: {environment}. Supported values are "production", "sandbox" and "test4".')

  def get_config(self):
    """
    Returns a copy of the current configuration dictionary.
    """
    return self._config.copy()  # Return a copy to avoid modification

environments = {
    "production": "https://gateway.vodapay.vodacom.co.za",
    "sandbox": "https://vodapay-gateway.sandbox.vfs.africa",
    "test4": "https://vodapay-gateway.test4.vfs.africa"
}

config = Configuration()  # Create a single instance of the configuration class
