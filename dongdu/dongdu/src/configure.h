#ifndef CONFIGURE_H_
#define CONFIGURE_H_

#include <string>
#include <set>

namespace dongdu {

	using namespace std;

	const char DEFAULT_SYL_FILE_PATH[] = "./data/VNsyl.txt";
	const char DEFAULT_WORDLIST_FILE_PATH[] = "./data/wordlist.txt";
	const char DEFAULT_MODEL_FILE_PATH[] = "./data/dongdu.model";
	const char DEFAULT_MAP_FILE_PATH[] = "./data/dongdu.map";
	const char SEPARATOR_CHAR = '/';

	const int MAX_WORD_LENGTH = 3;

	const char SPACE = ' ';
	const char UNDER = '_';
	const size_t LEARN   = 0;
	const size_t PREDICT = 1;
	const string SYMBOLS = "@`#$%&~|[]<>'(){}*+-=;,?.!:\"/";

	typedef pair<size_t, set<size_t>* > Feat;
	typedef size_t StrMapReference;
	typedef size_t FeatsReference;

} /* end of namespace */
#endif /* CONFIGURE_H_ */
