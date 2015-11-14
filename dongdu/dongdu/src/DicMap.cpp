/**
* @file DicMap.cpp
*/

#include "DicMap.h"
#include "configure.h"

using namespace std;
using namespace dongdu;

DicMap::DicMap()
{
	ifstream ifs(DEFAULT_WORDLIST_FILE_PATH);
	if (!ifs) {
		cout << "Failed to open file wordlist.txt" << endl;
		cout << "Please check again folder ./data" << endl;
		return;
	}
	string str;

	while(ifs && getline(ifs,str)) {
		dmap_.insert(pair<string, int> ( str , 1));
	}

	return;
}

DicMap::~DicMap()
{
	dmap_.clear();
	return;
}

bool DicMap::isWord(const string str)
{
	map<string, int>::iterator pos = dmap_.find(str);
	return (pos != dmap_.end());
}
