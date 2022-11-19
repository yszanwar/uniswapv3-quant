import warnings

class EndPoints():

    def __init__(self):
        #GraphQL pagination inital values
        self.step = 1000
        self.page = 0

        #Graph_QL_Endpoints
        self.mainnet_gql = "https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3"
        self.polygon_gql = "https://api.thegraph.com/subgraphs/name/ianlapham/uniswap-v3-polygon"
        self.optimism_gql = "https://api.thegraph.com/subgraphs/name/ianlapham/optimism-post-regenesis"
        self.arbitrum_gql = "https://api.thegraph.com/subgraphs/name/ianlapham/arbitrum-minimal"
        self.celo_gql = "https://api.thegraph.com/subgraphs/name/ianlapham/uniswap-celo"
        self.goerli_gql = "https://api.thegraph.com/subgraphs/name/ianlapham/uniswap-v3-gorli"

        #RPC Endpoints
        self.mainnet_rpc = "https://rpc.flashbots.net/"
        self.polygon_rpc = "https://polygon-rpc.com"
        self.optimism_rpc = "https://mainnet.optimism.io/"
        self.arbitrum_rpc = "https://rpc.ankr.com/arbitrum"
        self.celo_rpc = "https://forno.celo.org"
        self.goerli_rpc = "https://goerli.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161"
        pass
    

    def getGraphQLEndpoint(self, chain):
        warnings.warn("Warning: Using thegraph.com API endpoints.")
        if(chain=="mainnet"):
            return [self.mainnet_gql, self.step, self.page]
        if(chain=="polygon"):
            return [self.polygon_gql, self.step, self.page]
        if(chain=="optimism"):
            return [self.optimism_gql, self.step, self.page]
        if(chain=="arbitrum"):
            return [self.arbitrum_gql, self.step, self.page]
        if(chain=="celo"):
            return [self.celo_gql, self.step, self.page]
        if(chain=="goerli"):
            return [self.goerli_gql, self.step, self.page]
        print("No Chain Found")
        return 0
    
    def getRPCEndpoints(self, chain):
        warnings.warn("Warning: Using RPC API endpoints.")
        if(chain=="mainnet"):
            return self.mainnet_rpc
        if(chain=="polygon"):
            return self.polygon_rpc
        if(chain=="optimism"):
            return self.optimism_rpc
        if(chain=="arbitrum"):
            return self.arbitrum_rpc
        if(chain=="celo"):
            return self.celo_rpc
        if(chain=="goerli"):
            return self.goerli_rpc
        print("No Chain Found")
        return 0
