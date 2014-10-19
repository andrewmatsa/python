ISSUES_TYPE = ('BUG','ISSUE','ERROR')

def get_stat(text):

    return {type: text.count(type) for type in ISSUES_TYPE}
	
def get_warn_lines(text):
	#write code to count and return lines with warns
    tmp_sentences_list = text.replace("?", ".").replace("!", ".").split(".")
    sentences_list = []
    for sentence in tmp_sentences_list:
        for issue in ISSUES_TYPE:
            if sentence.count(issue) > 0:
                sentences_list.append(sentence)
    return sentences_list
 
def parse_text(**kwargs):
	'''
	Parse text and get stat
	'''

	text = kwargs["analyze"]
	stat, warns = get_stat(text), get_warn_lines(text)

	return (stat, warns)

def main():
	text = ("Today we got ISSUE on produciton that crashed our server."
	        "What is going on there? How much time can we wait for this ERROR to be resolved?"
	        "Finally, ISSUE-123 is resolved and we can go next with out business client."
	        "Phew!	Ok let's do following, if there is BUG on production then fire all stuff in Bangalore."
	        "Otherwise we will have huge lose. Will see how it will be!")

	(stat,warns) = parse_text(analyze=text)
	
	print "\nStatistics on issues %r:\n" % str(ISSUES_TYPE)
	for k,v in stat.iteritems():
		print "\tFound %r occurred %r times" % (k,stat[k])
	
	print "\nFound %r sentences:\n" % len(warns)
	for line in warns:
		print "\tFound issue here: %s" % line
 
if __name__ == "__main__":
    main()