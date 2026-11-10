from marlowe_index.index import Clause, ClauseIndex


def test_search_filters_language():
    index = ClauseIndex()
    index.add(Clause("c1", "en", "termination notice period"))
    index.add(Clause("c2", "fr", "periode de preavis"))
    assert [c.clause_id for c in index.search("notice", "en")] == ["c1"]
