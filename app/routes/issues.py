from fastapi import APIRouter, HTTPException, status
import uuid

from app.schemas import IssueCreate, IssueUpdate, IssueOut

from app.storage import load_data, save_data

router = APIRouter(prefix="/api/v1/issues", tags=["issues"])

@router.get("/", response_model=list[IssueOut])
async def get_issues():
    issues = load_data()

    return issues



@router.post("/", response_model=IssueOut, status_code=status.HTTP_201_CREATED)
async def create_issue(issue: IssueCreate):
    issues = load_data()

    new_issue = {
        "id": int(uuid.uuid4()),
        "title": issue.title,
        "description": issue.description,
        "status": "open",
        "priority": issue.priority.value,
    }

    issues.append(new_issue)
    save_data(issues)

    return new_issue

@router.get("/{issue_id}", response_model=IssueOut)
def get_issue(issue_id: int):
    issues = load_data()
    for issue in issues:
        if issue["id"] == issue_id:
            return issue
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")


@router.put("/{issue_id}", response_model=IssueOut)
def update_issue(issue_id: int, issue_update: IssueUpdate):
    issues = load_data()
    for issue in issues:
        if issue["id"] == issue_id:
            if issue_update.title is not None:
                issue["title"] = issue_update.title
            if issue_update.description is not None:
                issue["description"] = issue_update.description
            if issue_update.status is not None:
                issue["status"] = issue_update.status.value
            if issue_update.priority is not None:
                issue["priority"] = issue_update.priority.value

            save_data(issues)
            return issue

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")

@router.delete("/{issue_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_issue(issue_id: int):
    issues = load_data()
    for index, issue in enumerate(issues):
        if issue["id"] == issue_id:
            del issues[index]
            save_data(issues)
            return

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")




