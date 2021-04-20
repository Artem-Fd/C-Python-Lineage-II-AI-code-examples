#ifndef NET_H
#define NET_H

namespace net
{
    const int MN_CONNECTIONS=100;
    const int MS_RECIEVE_BUFFER=4096;
    const int serverPort=23;

    enum protocolG{P_NULL,TCP,UDP,P_E};

    enum iI{SOCKET,IP,PORT,I_E};
    enum oI{FLAGS,O_E};
    enum sI{S_E};

    typedef hTable<I_E,O_E,S_E>::structRow socketStruct;
}

class hNet
{
public:
    hNet();

};

class hServer
{
    SOCKET serverSocket=-1;

    struct sCompare{
        bool operator()(net::socketStruct aL, net::socketStruct bL) const { return aL.i[net::SOCKET] > bL.i[net::SOCKET];}
    };

    std::set<net::socketStruct, sCompare> s __attribute__((aligned(128)));

public:


    net::socketStruct acceptSocket()
    {
        sockaddr_in clientAddressL;
        net::socketStruct sRowL;
        
        int sizeClientAddressL=sizeof(clientAddressL);
        
        if (INVALID_SOCKET==(sRowL.i[net::SOCKET]=accept(serverSocket,(sockaddr*)&clientAddressL,&sizeClientAddressL)))
            throw hExeption(104,"Socket error (accept) ERROR="+WSAGetLastError(),"Net.h->hClient.acceptSocket()");
        else std::cout<<"Accept socket OK"<<std::endl;

        sRowL.i[net::IP]=clientAddressL.sin_addr.s_addr;
        sRowL.i[net::PORT]=ntohs(clientAddressL.sin_port);
        send(sRowL.i[net::SOCKET],"Accepted",sizeof("Accepted"),0);
        return sRowL;
        
    }

    hServer(uint32_t ipL, uint16_t portL, net::protocolG protocolL)
    {
        WSADATA wsaData;
        if (WSAStartup(0x202,&wsaData))
            throw hExeption(100,"Socket error (startup) ERROR="+WSAGetLastError(),"Net.h->hServer.hServer(uint32_t, uint16_t, net::protocol)");
        else std::cout<<"Start  ok"<<std::endl;

        SOCKET socketL;
        socketL = socket(AF_INET,protocolL,0);

        if (INVALID_SOCKET==(serverSocket=socket(AF_INET,protocolL,0)))
            throw hExeption(101,"Socket error (socket) INVALID_SOCKET, ERROR="+WSAGetLastError(),"Net.h->hServer.hServer(uint32_t, uint16_t, net::protocol)");
        else std::cout << "Create socket OK"<<std::endl;

        sockaddr_in serverAddress;
        serverAddress.sin_family=AF_INET;
        serverAddress.sin_port=htons(portL);
        serverAddress.sin_addr.s_addr=0;//ipL; // слушаем все IP с указанного порта

        if (SOCKET_ERROR==(bind(socketL,(sockaddr*)&serverAddress,sizeof(serverAddress))))
            throw hExeption(102,"Socket error (bind) ERROR="+WSAGetLastError(),"Net.h->hServer.hServer(uint32_t, uint16_t, net::protocol)");
        else std::cout<<"Bind OK"<<std::endl;

        if (SOCKET_ERROR==(listen(socketL,net::MN_CONNECTIONS)))
            throw hExeption(103,"Socket error (listen) ERROR="+WSAGetLastError(),"Net.h->hServer.hServer(uint32_t, uint16_t, net::protocol)");
        else std::cout<<"Listen OK"<<std::endl;

        serverSocket=socketL;
    };

};

class hClient
{
    struct cCompare{
        bool operator()(net::socketStruct aL, net::socketStruct bL) const { return aL.i[net::SOCKET] > bL.i[net::SOCKET];}
    };

    std::set<net::socketStruct, cCompare> c __attribute__((aligned(128)));

public:


    net::socketStruct connectSocket(uint32_t ipL, uint16_t portL, net::protocolG protocolL)
    {
        SOCKET clientSocketL;
        net::socketStruct cRowL;

        if (INVALID_SOCKET==(clientSocketL=socket(AF_INET,protocolL,0)))
            throw hExeption(104,"Socket error (socket) ERROR="+WSAGetLastError(),"Net.h->hClient.connectSocket(uint32_t, uint16_t, net::protocol)");
        else std::cout<<"Create socket OK"<<std::endl;

        sockaddr_in clientAddressL;
        clientAddressL.sin_family=AF_INET;
        clientAddressL.sin_port=htons(portL);
        clientAddressL.sin_addr.s_addr=ipL;

        if (SOCKET_ERROR==connect(clientSocketL,(sockaddr *)&clientAddressL,sizeof (clientAddressL)))
            throw hExeption(105,"Socket error (connect) ERROR="+WSAGetLastError(),"Net.h->hClient.connectSocket(uint32_t, uint16_t, net::protocol)");
        else std::cout<<"Connect OK"<<std::endl;

        cRowL.i[net::SOCKET]=clientSocketL;
        cRowL.i[net::IP]=clientAddressL.sin_addr.s_addr;
        cRowL.i[net::PORT]=ntohs(clientAddressL.sin_port);

        return cRowL;
    }

    hClient(int parameterL){};


};

void acceptWrapper(hServer &srv)
{
    while(true)
    {
    srv.acceptSocket();//
    }
}

std::ostream& operator<<(std::ostream& os, const net::socketStruct& aL)
{
    in_addr iL;
    iL.s_addr=aL.i[net::IP];

    os <<"SOCKET:"<<aL.i[net::SOCKET]<<" IP:"<<inet_ntoa(iL)<<" PORT:"<<aL.i[net::PORT];
    return os;
}
#endif // NET_H
