from __future__ import annotations
from typing import Any
import requests

DEFAULT_STUDY_TYPES = [
    "systematic_review",
    "meta_analysis",
    "randomized_controlled_trial",
    "cohort_study",
]
# We will treat standard NCBI study typs basically, but typically it's returned under pubtype

def build_search_queries(title: str) -> list[str]:
    return [
        f"{title} systematic review",
        f"{title} clinical trial",
    ]

def search_pubmed_ids(query: str, retmax: int = 5) -> list[str]:
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": retmax,
        "retmode": "json"
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data.get("esearchresult", {}).get("idlist", [])

def fetch_pubmed_summaries(pmids: list[str]) -> list[dict[str, Any]]:
    if not pmids:
        return []
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
    params = {
        "db": "pubmed",
        "id": ",".join(pmids),
        "retmode": "json"
    }
    response = requests.get(url, params=params)
    data = response.json()
    result = data.get("result", {})
    uids = result.get("uids", [])
    
    summaries = []
    for uid in uids:
        doc = result.get(uid, {})
        title = doc.get("title", "")
        pubdate = doc.get("pubdate", "")
        year = pubdate.split(" ")[0] if pubdate else "unknown"
        # Determine study type heuristically for mock purposes if pubtype is missing
        pubtypes = doc.get("pubtype", [])
        study_type = "observational"
        if any("review" in pt.lower() for pt in pubtypes):
            study_type = "systematic_review"
        elif any("trial" in pt.lower() for pt in pubtypes):
            study_type = "randomized_controlled_trial"
        
        summaries.append({
            "title": title,
            "year": year,
            "study_type": study_type,
            "main_finding": "Abstract data is not extracted by basic esummary. Needs efetch for full abstract.",
            "important_limitation": "PubMed ESummary API only provides titles."
        })
    return summaries


def research_topic(plan: dict[str, Any]) -> dict[str, Any]:
    """Create structured starter research notes for a topic using english queries."""
    title = plan.get("topic", "Untitled topic")
    queries = plan.get("english_search_queries", [f"{title} clinical trial"])

    pmids: list[str] = []
    for query in queries:
        ids = search_pubmed_ids(query, retmax=5)
        pmids.extend(ids)

    # dedup PMID sambil jaga urutan
    seen = set()
    unique_pmids = []
    for pmid in pmids:
        if pmid not in seen:
            seen.add(pmid)
            unique_pmids.append(pmid)

    selected_sources = fetch_pubmed_summaries(unique_pmids[:8])

    return {
        "topic": title,
        "search_queries": queries,
        "selected_sources": selected_sources,
        "recommended_study_types": DEFAULT_STUDY_TYPES
    }