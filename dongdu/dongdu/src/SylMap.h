/**
* @file SylMap.h
*/
#ifndef SYLMAP_H_
#define SYLMAP_H_

#include <fstream>
#include <set>
#include <string>
#include <iostream>

namespace dongdu {
	using namespace std;

	class SylMap {
	private:
		set<string> _syl;
	public:
		SylMap();
		virtual ~SylMap();
		bool isVNESE(string syllabel);
	};

} /* namespace dongdu */
#endif /* SYLMAP_H_ */
