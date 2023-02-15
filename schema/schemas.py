from pydantic import BaseModel, EmailStr, HttpUrl, validator, Field, Required, Json
from typing import Union, Dict, Any
from datetime import datetime, date
from common.messages import Messages
from fastapi import Query
import re
from uuid import UUID

current_date = datetime.now()


class ApprovalStagingModel(BaseModel):
    created_by: int
    role_id: int
    admin_comment: str = None
    description: str = None


class admin_(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr


class admin_role(BaseModel):
    role_id: int
    approval: Union[ApprovalStagingModel]


class faq_id(BaseModel):
    id: int


class GoogleLogin(BaseModel):
    access_token: str
    id_token: str
    googleId: str
    email: EmailStr
    givenName: str
    familyName: str
    imageUrl: HttpUrl


class CategorySchema(BaseModel):
    category_name: str


class cat_(BaseModel):
    category: Union[CategorySchema]
    approval: Union[ApprovalStagingModel]


class ZipUpdateSchema(BaseModel):
    zip_code: str = Field(default=Required, max_length=5, min_length=5)
    city: str = Field(default=Required, min_length=1, max_length=30)


class zipcity_(BaseModel):
    zipupdate: Union[ZipUpdateSchema]
    approval: Union[ApprovalStagingModel]


class ZipcityAdd(BaseModel):
    zip_add: Union[ZipUpdateSchema]
    approval: Union[ApprovalStagingModel]


class school_(BaseModel):
    school: str


class SchoolAdd(BaseModel):
    sch_add: Union[school_]
    approval: Union[ApprovalStagingModel]


class SchoolUpdate(BaseModel):
    schoolupdate: Union[school_]
    approval: Union[ApprovalStagingModel]


class MajorSchema(BaseModel):
    major: str


class major_(BaseModel):
    majorupdate: Union[MajorSchema]
    approval: Union[ApprovalStagingModel]


class MajorAdd(BaseModel):
    maj_add: Union[MajorSchema]
    approval: Union[ApprovalStagingModel]


class OccupationSchema(BaseModel):
    occupation: str


class OccupationAdd(BaseModel):
    occ_add: Union[OccupationSchema]
    approval: Union[ApprovalStagingModel]


class occupation_(BaseModel):
    occ_update: Union[OccupationSchema]
    approval: Union[ApprovalStagingModel]


class SelfOccupationSchema(BaseModel):
    self_occupation: str


class SelfOccupationAdd(BaseModel):
    self_add: Union[SelfOccupationSchema]
    approval: Union[ApprovalStagingModel]


class self_occupation_(BaseModel):
    self_update: Union[SelfOccupationSchema]
    approval: Union[ApprovalStagingModel]


class faq_(BaseModel):
    category_id: int
    question: str
    answer: str


class FaqAdd(BaseModel):
    faqadd: Union[faq_]
    approval: Union[ApprovalStagingModel]


class faq_edit_(BaseModel):
    question: str
    answer: str


class FaqUpdate(BaseModel):
    faq_update: Union[faq_edit_]
    approval: Union[ApprovalStagingModel]


class FaqPosition(BaseModel):
    position: int


class CreateAdmin(BaseModel):
    role_id: str
    email: EmailStr


class PutVersion(BaseModel):
    version_name: str
    version_code: float
    minimum_os_version: float
    release_date: str
    skip_update: str
    is_update_live: str
    version_description: str
    row_id: int
    approval: Union[ApprovalStagingModel]


class SwitchMaintenance(BaseModel):
    os_type: int
    mode: bool
    approval: Union[ApprovalStagingModel]


class PostMakerChecker(BaseModel):
    id: int
    action_performed: int
    done_by: int
    role_id: int
    module_name: int
    description: str
    row_id: int
    data_json: Dict[str, Any] = {}
    table_name: str
    approved_by: int
    admin_comment: str
    created_date: datetime
    modified_date: datetime
    created_by: int
    modified_by: int


class PutNeuInfo(BaseModel):
    id: int
    email: str
    phone_number: int
    # created_date: datetime = current_date
    # modified_date: datetime = None
    # created_by: int = 1
    # modified_by: int = None


class NeuInfoUpdate(BaseModel):
    neuinfo_update: Union[PutNeuInfo]
    approval: Union[ApprovalStagingModel]

class AuthorizeActivity(BaseModel):
    rejection_message: str = None


class DeactivateMessage(BaseModel):
    deactivate_reason: str = None
    row_id: int
    approval: Union[ApprovalStagingModel]


class PermissionsSchema(BaseModel):
    create_administrators: bool = Field(default=Required)
    view_administrators: bool = Field(default=Required)
    update_administrators: bool = Field(default=Required)
    view_users: bool = Field(default=Required)
    deactivate_users: bool = Field(default=Required)
    view_approved_users: bool = Field(default=Required)
    deactivate_approved_users: bool = Field(default=Required)
    view_pending_users: bool = Field(default=Required)
    deactivate_pending_users: bool = Field(default=Required)
    view_rejected_users: bool = Field(default=Required)
    deactivate_rejected_users: bool = Field(default=Required)
    view_not_applied_users: bool = Field(default=Required)
    deactivate_not_applied_users: bool = Field(default=Required)
    view_delinquent_users: bool = Field(default=Required)
    deactivate_delinquent: bool = Field(default=Required)
    view_state_list: bool = Field(default=Required)
    deactivate_state: bool = Field(default=Required)
    view_city_zip_code: bool = Field(default=Required)
    add_city_zip_code: bool = Field(default=Required)
    update_city_zip_code: bool = Field(default=Required)
    deactivate_city_zip_code: bool = Field(default=Required)
    view_school_list: bool = Field(default=Required)
    add_school: bool = Field(default=Required)
    update_school: bool = Field(default=Required)
    deactivate_school: bool = Field(default=Required)
    view_major_list: bool = Field(default=Required)
    add_major: bool = Field(default=Required)
    update_major: bool = Field(default=Required)
    deactivate_major: bool = Field(default=Required)
    view_occupation_list: bool = Field(default=Required)
    add_occupation: bool = Field(default=Required)
    update_occupation: bool = Field(default=Required)
    deactivate_occupation: bool = Field(default=Required)
    view_self_occupation_list: bool = Field(default=Required)
    add_self_occupation: bool = Field(default=Required)
    update_self_occupation: bool = Field(default=Required)
    deactivate_self_occupation: bool = Field(default=Required)
    view_faqs: bool = Field(default=Required)
    update_faqs: bool = Field(default=Required)
    deactivate_faqs: bool = Field(default=Required)
    sort_faqs: bool = Field(default=Required)
    view_category_list: bool = Field(default=Required)
    update_category: bool = Field(default=Required)
    deactivate_category: bool = Field(default=Required)
    view_feedbacks: bool = Field(default=Required)
    view_maintenance_list: bool = Field(default=Required)
    add_maintenance: bool = Field(default=Required)
    deactivate_maintenance: bool = Field(default=Required)
    view_version_information: bool = Field(default=Required)
    add_version_information: bool = Field(default=Required)
    update_version_information: bool = Field(default=Required)
    deactivate_version_information: bool = Field(default=Required)
    view_screens_data: bool = Field(default=Required)
    view_neu_information: bool = Field(default=Required)
    update_neu_information: bool = Field(default=Required)
    deactivate_administrator: bool
    add_category: bool
    add_faqs: bool
    update_maintenance: bool


class AdminPermissions(BaseModel):
    admin: Union[PermissionsSchema, None]
    owner: Union[PermissionsSchema, None]
    read_only: Union[PermissionsSchema, None]


class PostAdminRoles(BaseModel):
    config_perm: Union[AdminPermissions, None]
    created_by: int
    modified_by: int


class AddUserData(BaseModel):
    user_uuid: UUID = Field(default=Required)
    first_name: str = Field(default=Required)
    last_name: str = Field(default=Required)
    email: str = Field(default=Required)
    phone_number: int = Field(default=Required)
    state_code: str = Field(default=Required)
    cc_status_code: int = Field(default=Required)
    ssn_number: str = Field(default=Required)
    locked_status: bool = Field(default=Required)
    device_brand_name: str = Field(default=Required)
    device_os_version: str = Field(default=Required)
    date_of_birth: date = Field(default=Required)
    address_pri_id: int = Field(default=Required)
    address_ship_id: int = Field(default=Required)
    user_citizenship_id: int = Field(default=Required)
    employement_details_id: int = Field(default=Required)
    education_details_id: int = Field(default=Required)
    last_login: datetime = Field(default=Required)
    registered_at: datetime = Field(default=Required)
    deleted_at: datetime = Field(default=Required)


class AddFeedbackData(BaseModel):
    user_uuid: UUID = Field(default=Required)
    feedback_rating: Dict = Field(default=Required)


class UpdateUserDetails(BaseModel):
    phone_number: int = None
    email: str = None


responses = {
    400: {"description": "invalid request headers",
          "content": {
              "application/json": {
                  "example": {"code": 400, "message": Messages.INVALID_REQUEST_HEADERS, "errors": []}
              }}},
    401: {"description": "Authorization token is Invalid/expired",
          "content": {
              "application/json": {
                  "example": {"code": 401, "message": Messages.AUTHORIZATION_FAILED}
              }}},
    406: {"description": "Account Deactivated",
          "content": {
              "application/json": {
                  "example": {"code": 406, "message": Messages.ACCOUNT_DEACTIVATED}
              }}},

    500: {"description": "Internal Server Error",
          "content": {
              "application/json": {
                  "example": {"code": 500, "message": Messages.SOMETHING_WENT_WRONG}
              }}},
}