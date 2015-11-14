/**
* @file SylMap.cpp
*/
#include "SylMap.h"
#include "configure.h"

using namespace std;

namespace dongdu {

SylMap::SylMap()
{
	_syl.clear();

	ifstream ifs(DEFAULT_SYL_FILE_PATH);

	if (!ifs) {
		cout << "Failed to open file VNsyl.txt" << endl;
		return;
	}

	int N;
	ifs >> N;

	string str;
	for(int i = 0; i < N; ++i) {
		ifs >> str;
		_syl.insert(str);
	}

	return;
}

SylMap::~SylMap() {
	_syl.clear();
}

bool SylMap::isVNESE(string syllabel)
{
	set<string>::iterator it;
	it = _syl.find(syllabel);
	return (it != _syl.end());
}

} /* namespace dongdu */
