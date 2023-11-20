/*  File: backHelper.h
*   Author: STUDENT
*   Date: 
*   Description: 
*              
*              
*/

#include <netinet/in.h>
#include "../buildAndConfig/functionality.h"

/*====== Macros =======*/

/* default snap length (maximum bytes per packet to capture) */
#define SNAP_LEN 

/* ethernet headers are always exactly X bytes */
#define SIZE_ETHERNET 

/* Ethernet addresses are X bytes */
#define ETHER_ADDR_LEN 


/*====== Functions =======*/

// Verify and keep track of successful port knocks. Then call the corresponding functions
void got_packet(u_char *args, const struct pcap_pkthdr *header, const u_char *packet);

// gets called when the single knock port option is activated.
void singleKnock();

// multiple knocked ports
void multiKnock();


/*====== Networking Structs =======*/

/* Ethernet header */
struct sniff_ethernet {
// TODO
};

/* IP header */
struct sniff_ip {
// TODO
};

#define IP_HL(ip) // TODO
#define IP_V(ip)  // TODO

/* TCP header */
typedef u_int tcp_seq;

struct sniff_tcp {
// TODO
};
