import warnings

class EndPoints():
    
    #GraphQL pagination
    step = 1000
    page = 0

    mainnet_gql = "https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3"
    polygon_gql = "https://api.thegraph.com/subgraphs/name/ianlapham/uniswap-v3-polygon"
    optimism_gql = "https://api.thegraph.com/subgraphs/name/ianlapham/optimism-post-regenesis"
    arbitrum_gql = "https://api.thegraph.com/subgraphs/name/ianlapham/arbitrum-minimal"
    celo_gql = "https://api.thegraph.com/subgraphs/name/ianlapham/uniswap-celo"
    goerli_gql = "https://api.thegraph.com/subgraphs/name/ianlapham/uniswap-v3-gorli"

    mainnet_rpc = "https://rpc.flashbots.net/"
    polygon_rpc = "https://polygon-rpc.com"
    optimism_rpc = "https://mainnet.optimism.io/"
    arbitrum_rpc = "https://rpc.ankr.com/arbitrum"
    celo_rpc = "https://forno.celo.org"
    goerli_rpc = "https://goerli.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161"

    def getGraphQLEndpoint(chain):
        warnings.warn("Warning: Using thegraph.com API endpoints.")
        if(chain=="mainnet"):
            return EndPoints.mainnet_gql
        if(chain=="polygon"):
            return EndPoints.mainnet_gql
        if(chain=="optimism"):
            return EndPoints.optimism_gql
        if(chain=="arbitrum"):
            return EndPoints.arbitrum_gql
        if(chain=="celo"):
            return EndPoints.celo_gql
        if(chain=="goerli"):
            return EndPoints.goerli_gql
        print("No Chain Found")
        return 0
    
    def getRPCEndpoints(chain):
        warnings.warn("Warning: Using thegraph.com API endpoints.")
        if(chain=="mainnet"):
            return EndPoints.mainnet_rpc
        if(chain=="polygon"):
            return EndPoints.mainnet_rpc
        if(chain=="optimism"):
            return EndPoints.optimism_rpc
        if(chain=="arbitrum"):
            return EndPoints.arbitrum_rpc
        if(chain=="celo"):
            return EndPoints.celo_rpc
        if(chain=="goerli"):
            return EndPoints.goerli_rpc
        print("No Chain Found")
        return 0
