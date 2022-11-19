import pandas as pd
import requests

class PoolState():

    def __init__(self, chain, address):
        self.chain = chain
        self.address = address
        self.ticksState_df = pd.DataFrame()
        self.ticksFlow_df = pd.DataFrame()


    def __createQuery(self, type, address, graphQl_endpoints):


        if(type=="PoolDetails"):
            query = """
            {
                pool(id: \""""+address+"""\"){
                    
                    id
                    
                    token0 {
                        id
                        symbol
                        name
                        decimals
                    }
                    
                    token1 {
                        id
                        symbol
                        name
                        decimals
                    }
                    
                    feeTier
                    tick
                    totalValueLockedUSD
                    sqrtPrice
                    liquidity
                    }
                }
            
            """
        
        if(type=="TickState"):
        
            query = """
                {
            pool(id: \""""+address+"""\") {
                    ticks (orderBy: liquidityGross, orderDirection: desc, first: """+str(graphQl_endpoints[1])+""", skip: """+str(graphQl_endpoints[2])+""", where:{liquidityNet_gt: 0} ) {
                    tickIdx,
                liquidityNet
                liquidityGross
                feeGrowthOutside0X128
                feeGrowthOutside1X128
                        }
                    }
                }

            """


        if(type=="TickFlow"):
            query = """
            {
            pool(id: \""""+address+"""\"){
	            swaps (orderBy: timestamp, orderDirection: desc, first: """+str(graphQl_endpoints[1])+""", skip: """+str(graphQl_endpoints[2])+""") {
                tick
                timestamp
                amount0
                amount1
		            }
                }
            }
            """
        return query

    def getPoolDetails(self, graphQl_endpoints):
        
        #get pool state from subgraph API
        response = requests.post(graphQl_endpoints[0], json={'query': self.__createQuery("PoolDetails", self.address, graphQl_endpoints)}).json()
        poolDetails = response['data']['pool']

        return poolDetails


    def getTicksState(self, graphQl_endpoints):
        
        
        #New state dataframe
        self.ticksState_df = pd.DataFrame()

        #get ticks state from subgraph API
        while True:
            response  = requests.post(graphQl_endpoints[0], json={'query': self.__createQuery("TickState", self.address, graphQl_endpoints)}).json()
            if(len(response['data']['pool']['ticks'])>0):
                self.ticksState_df = self.ticksState_df.append(pd.json_normalize(response['data']['pool']['ticks']))
                graphQl_endpoints[2] = graphQl_endpoints[2] + graphQl_endpoints[1]
            else:
                break
        return self.ticksState_df

    def getTickFlow(self, graphQl_endpoints, tick_length):
        
        #New tickFlow dataframe
        self.ticksFlow_df = pd.DataFrame()

        #get ticks flow from subgraph API
        while (graphQl_endpoints[2]< tick_length):
            response  = requests.post(graphQl_endpoints[0], json={'query': self.__createQuery("TickFlow", self.address, graphQl_endpoints)}).json()
            if(len(response['data']['pool']['swaps'])>0):
                self.ticksFlow_df = self.ticksFlow_df.append(pd.json_normalize(response['data']['pool']['swaps']))
                graphQl_endpoints[2] = graphQl_endpoints[2] + graphQl_endpoints[1]
            else:
                break

        return self.ticksFlow_df




        
