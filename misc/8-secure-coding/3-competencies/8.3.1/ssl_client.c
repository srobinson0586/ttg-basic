#include "ssl_client.h"

/*
*  	Initialize all required SSL resources and wrap the socket with SSL in order to retrieve the
*	X509 certificate from "www.xkcd.com"
* 	params: 
*			none
*	returns:
*			int - status code
*/
int main(){
	return 0;
}


/* Used to send the GET request over the ssl connection to the https server
 * Parameters:
 *		char* req 	- the GET request string to send to the https server.
 *		SSL* ssl 	- the SSL context and connection to manage communicating with https server
 * Returns:
 *		int - returns a number that conveys whether or not there was an error.
 */
int send_packet(char* req, SSL* ssl){
	return -1;
}


/* Used to receive the response to the GET request from the https server
 * Parameters:
 *		SSL* ssl 	- the SSL context and connection to manage communicating with https server
 * Returns:
 *		int - returns a number that conveys whether or not there was an error.
 */
int recv_packet(SSL* ssl){
	return -1;
}

/*
*  	Creates connection to the given port at the provided website.
* 	params: 
*			char* website - The website to establish connection to. "www.xkcd.com"
*			int port	  - The port to connect to. For https it's 443
*	returns:
*			int - The file descriptor for the socket the conection was created on
*/
int create_connection(char* website, int port){
	return -1;
}