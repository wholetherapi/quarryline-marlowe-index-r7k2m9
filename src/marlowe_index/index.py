"""Small multilingual clause index."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Clause:
    clause_id: str
    language: str
    text: str


class ClauseIndex:
    def __init__(self) -> None:
        self._clauses: dict[str, Clause] = {}

    def add(self, clause: Clause) -> None:
        self._clauses[clause.clause_id] = clause

    def search(self, terms: str, language: str | None = None) -> list[Clause]:
        needles = [term for term in terms.lower().split() if term]
        hits = []
        for clause in self._clauses.values():
            if language is not None and clause.language != language:
                continue
            haystack = clause.text.lower()
            if all(needle in haystack for needle in needles):
                hits.append(clause)
        return hits
