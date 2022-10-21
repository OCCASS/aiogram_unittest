from typing import Any
from typing import Dict
from typing import Sequence


class ArgumentsParser:
    @classmethod
    def _get_async_mock_args(cls, keys: Sequence, call_args) -> Dict[str, Any]:
        result_data = {k: None for k in keys}

        if call_args is None:
            return result_data

        args, kwargs = call_args.args, call_args.kwargs
        for index, arg in enumerate(args):
            key_name = keys[index]
            result_data[key_name] = arg

        for key_name, arg in kwargs.items():
            result_data[key_name] = arg

        return result_data

    @classmethod
    def get_answer_callback_query_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("callback_query_id", "text", "show_alert", "url", "cache_time")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_copy_message_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = (
            "chat_id",
            "from_chat_id",
            "message_id",
            "caption",
            "parse_mode",
            "caption_entities",
            "disable_notification",
            "protect_content",
            "reply_to_message_id",
            "allow_sending_without_reply",
            "reply_markup",
            "payload",
            "result",
        )
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_create_chat_invite_link_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("chat_id", "expire_date", "member_limit", "name", "creates_join_request", "payload", "result")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_create_invoice_link_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = (
            "title",
            "description",
            "payload",
            "provider_token",
            "currency",
            "prices",
            "max_tip_amount",
            "suggested_tip_amounts",
            "provider_data",
            "photo_url",
            "photo_size",
            "photo_width",
            "photo_height",
            "need_name",
            "need_phone_number",
            "need_email",
            "need_shipping_address",
            "send_phone_number_to_provider",
            "send_email_to_provider",
            "is_flexible",
        )
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_create_new_sticker_set_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = (
            "user_id",
            "name",
            "title",
            "emojis",
            "png_sticker",
            "tgs_sticker",
            "webm_sticker",
            "contains_masks",
            "sticker_type",
            "mask_position",
            "payload",
            "files",
        )
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_decline_chat_join_request_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("chat_id", "user_id", "payload")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_delete_chat_photo_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("chat_id", "payload")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_delete_chat_sticker_set_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("chat_id", "payload")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_delete_message_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("chat_id", "message_id", "payload")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_delete_my_commands_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("scope", "language_code", "payload")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_delete_sticker_from_set_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("sticker", "payload")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_delete_webhook_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("drop_pending_updates", "payload")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_download_file_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = (
            "file_path",
            "destination",
            "timeout",
            "chunk_size",
            "seek",
            "destination_dir",
            "make_dirs",
            "url",
            "dest",
            "session",
            "response",
            "chunk",
        )
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_download_file_by_id_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("file_id", "destination", "timeout", "chunk_size", "seek", "destination_dir", "make_dirs", "file")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_edit_chat_invite_link_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = (
            "chat_id",
            "invite_link",
            "expire_date",
            "member_limit",
            "name",
            "creates_join_request",
            "payload",
            "result",
        )
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_edit_message_caption_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = (
            "chat_id",
            "message_id",
            "inline_message_id",
            "caption",
            "parse_mode",
            "caption_entities",
            "reply_markup",
            "payload",
            "result",
        )
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_edit_message_live_location_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = (
            "latitude",
            "longitude",
            "chat_id",
            "message_id",
            "inline_message_id",
            "horizontal_accuracy",
            "heading",
            "proximity_alert_radius",
            "reply_markup",
            "payload",
            "result",
        )
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_edit_message_media_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("media", "chat_id", "message_id", "inline_message_id", "reply_markup", "payload", "files", "result")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_edit_message_reply_markup_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("chat_id", "message_id", "inline_message_id", "reply_markup", "payload", "result")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_edit_message_text_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = (
            "text",
            "chat_id",
            "message_id",
            "inline_message_id",
            "parse_mode",
            "entities",
            "disable_web_page_preview",
            "reply_markup",
            "payload",
            "result",
        )
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_export_chat_invite_link_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("chat_id", "payload")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_forward_message_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("chat_id", "from_chat_id", "message_id", "disable_notification", "protect_content", "payload", "result")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_get_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("key", "default")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_get_chat_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("chat_id", "payload", "result")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_get_chat_administrators_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("chat_id", "payload", "result")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_get_chat_member_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("chat_id", "user_id", "payload", "result")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_get_chat_member_count_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("chat_id", "payload")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_get_chat_members_count_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("chat_id",)
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_get_chat_menu_button_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("chat_id", "payload", "result")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_get_current_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("no_error",)
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_get_custom_emoji_stickers_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("custom_emoji_ids", "payload", "result")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_get_file_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("file_id", "payload", "result")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_get_file_url_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("file_path",)
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_get_game_high_scores_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("user_id", "chat_id", "message_id", "inline_message_id", "payload", "result")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_get_me_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("payload", "result")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_get_my_commands_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("scope", "language_code", "payload", "result")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_get_my_default_administrator_rights_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("for_channels", "payload", "result")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_get_new_session_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ()
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_get_session_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ()
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_get_sticker_set_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("name", "payload", "result")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_get_updates_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("offset", "limit", "timeout", "allowed_updates", "payload", "result")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_get_user_profile_photos_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("user_id", "offset", "limit", "payload", "result")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_get_webhook_info_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("payload", "result")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_kick_chat_member_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("chat_id", "user_id", "until_date", "revoke_messages")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_leave_chat_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("chat_id", "payload")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_log_out_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("payload",)
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_pin_chat_message_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("chat_id", "message_id", "disable_notification", "payload")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_promote_chat_member_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = (
            "chat_id",
            "user_id",
            "is_anonymous",
            "can_manage_chat",
            "can_change_info",
            "can_post_messages",
            "can_edit_messages",
            "can_delete_messages",
            "can_manage_voice_chats",
            "can_invite_users",
            "can_restrict_members",
            "can_pin_messages",
            "can_promote_members",
            "can_manage_video_chats",
            "payload",
        )
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_request_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("method", "data", "files", "kwargs")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_request_timeout_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("kwds",)
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_restrict_chat_member_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = (
            "chat_id",
            "user_id",
            "permissions",
            "until_date",
            "can_send_messages",
            "can_send_media_messages",
            "can_send_other_messages",
            "can_add_web_page_previews",
            "payload",
            "permission",
        )
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_revoke_chat_invite_link_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("chat_id", "invite_link", "payload", "result")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_send_animation_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = (
            "chat_id",
            "animation",
            "duration",
            "width",
            "height",
            "thumb",
            "caption",
            "parse_mode",
            "caption_entities",
            "disable_notification",
            "protect_content",
            "reply_to_message_id",
            "allow_sending_without_reply",
            "reply_markup",
            "payload",
            "files",
            "result",
        )
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_send_audio_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = (
            "chat_id",
            "audio",
            "caption",
            "parse_mode",
            "caption_entities",
            "duration",
            "performer",
            "title",
            "thumb",
            "disable_notification",
            "protect_content",
            "reply_to_message_id",
            "allow_sending_without_reply",
            "reply_markup",
            "payload",
            "files",
            "result",
        )
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_send_chat_action_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("chat_id", "action", "payload")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_send_contact_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = (
            "chat_id",
            "phone_number",
            "first_name",
            "last_name",
            "vcard",
            "disable_notification",
            "protect_content",
            "reply_to_message_id",
            "allow_sending_without_reply",
            "reply_markup",
            "payload",
            "result",
        )
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_send_dice_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = (
            "chat_id",
            "disable_notification",
            "protect_content",
            "emoji",
            "reply_to_message_id",
            "allow_sending_without_reply",
            "reply_markup",
            "payload",
            "result",
        )
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_send_document_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = (
            "chat_id",
            "document",
            "thumb",
            "caption",
            "parse_mode",
            "caption_entities",
            "disable_content_type_detection",
            "disable_notification",
            "protect_content",
            "reply_to_message_id",
            "allow_sending_without_reply",
            "reply_markup",
            "payload",
            "files",
            "result",
        )
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_send_file_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("file_type", "method", "file", "payload", "files")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_send_game_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = (
            "chat_id",
            "game_short_name",
            "disable_notification",
            "protect_content",
            "reply_to_message_id",
            "allow_sending_without_reply",
            "reply_markup",
            "payload",
            "result",
        )
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_send_invoice_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = (
            "chat_id",
            "title",
            "description",
            "payload",
            "provider_token",
            "currency",
            "prices",
            "max_tip_amount",
            "suggested_tip_amounts",
            "start_parameter",
            "provider_data",
            "photo_url",
            "photo_size",
            "photo_width",
            "photo_height",
            "need_name",
            "need_phone_number",
            "need_email",
            "need_shipping_address",
            "send_phone_number_to_provider",
            "send_email_to_provider",
            "is_flexible",
            "disable_notification",
            "protect_content",
            "reply_to_message_id",
            "allow_sending_without_reply",
            "reply_markup",
            "payload_",
            "result",
        )
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_send_location_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = (
            "chat_id",
            "latitude",
            "longitude",
            "horizontal_accuracy",
            "live_period",
            "heading",
            "proximity_alert_radius",
            "disable_notification",
            "protect_content",
            "reply_to_message_id",
            "allow_sending_without_reply",
            "reply_markup",
            "payload",
            "result",
        )
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_send_media_group_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = (
            "chat_id",
            "media",
            "disable_notification",
            "protect_content",
            "reply_to_message_id",
            "allow_sending_without_reply",
            "files",
            "payload",
            "result",
        )
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_send_message_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = (
            "chat_id",
            "text",
            "parse_mode",
            "entities",
            "disable_web_page_preview",
            "disable_notification",
            "protect_content",
            "reply_to_message_id",
            "allow_sending_without_reply",
            "reply_markup",
            "payload",
            "result",
        )
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_send_photo_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = (
            "chat_id",
            "photo",
            "caption",
            "parse_mode",
            "caption_entities",
            "disable_notification",
            "protect_content",
            "reply_to_message_id",
            "allow_sending_without_reply",
            "reply_markup",
            "payload",
            "files",
            "result",
        )
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_send_poll_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = (
            "chat_id",
            "question",
            "options",
            "is_anonymous",
            "type",
            "allows_multiple_answers",
            "correct_option_id",
            "explanation",
            "explanation_parse_mode",
            "explanation_entities",
            "open_period",
            "close_date",
            "is_closed",
            "disable_notification",
            "protect_content",
            "reply_to_message_id",
            "allow_sending_without_reply",
            "reply_markup",
            "payload",
            "result",
        )
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_send_sticker_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = (
            "chat_id",
            "sticker",
            "disable_notification",
            "protect_content",
            "reply_to_message_id",
            "allow_sending_without_reply",
            "reply_markup",
            "payload",
            "files",
            "result",
        )
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_send_venue_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = (
            "chat_id",
            "latitude",
            "longitude",
            "title",
            "address",
            "foursquare_id",
            "foursquare_type",
            "google_place_id",
            "google_place_type",
            "disable_notification",
            "protect_content",
            "reply_to_message_id",
            "allow_sending_without_reply",
            "reply_markup",
            "payload",
            "result",
        )
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_send_video_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = (
            "chat_id",
            "video",
            "duration",
            "width",
            "height",
            "thumb",
            "caption",
            "parse_mode",
            "caption_entities",
            "supports_streaming",
            "disable_notification",
            "protect_content",
            "reply_to_message_id",
            "allow_sending_without_reply",
            "reply_markup",
            "payload",
            "files",
            "result",
        )
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_send_video_note_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = (
            "chat_id",
            "video_note",
            "duration",
            "length",
            "thumb",
            "disable_notification",
            "protect_content",
            "reply_to_message_id",
            "allow_sending_without_reply",
            "reply_markup",
            "payload",
            "files",
            "result",
        )
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_send_voice_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = (
            "chat_id",
            "voice",
            "caption",
            "parse_mode",
            "caption_entities",
            "duration",
            "disable_notification",
            "protect_content",
            "reply_to_message_id",
            "allow_sending_without_reply",
            "reply_markup",
            "payload",
            "files",
            "result",
        )
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_set_chat_administrator_custom_title_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("chat_id", "user_id", "custom_title", "payload")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_set_chat_description_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("chat_id", "description", "payload")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_set_chat_menu_button_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("chat_id", "menu_button", "payload")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_set_chat_permissions_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("chat_id", "permissions", "payload")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_set_chat_photo_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("chat_id", "photo", "payload", "files")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_set_chat_sticker_set_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("chat_id", "sticker_set_name", "payload")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_set_chat_title_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("chat_id", "title", "payload")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_set_current_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("value",)
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_set_game_score_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = (
            "user_id",
            "score",
            "force",
            "disable_edit_message",
            "chat_id",
            "message_id",
            "inline_message_id",
            "payload",
            "result",
        )
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_set_my_commands_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("commands", "scope", "language_code", "payload")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_set_my_default_administrator_rights_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("rights", "for_channels", "payload")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_set_passport_data_errors_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("user_id", "errors", "payload")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_set_sticker_position_in_set_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("sticker", "position", "payload")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_set_sticker_set_thumb_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("name", "user_id", "thumb", "payload", "files")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_set_webhook_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = (
            "url",
            "certificate",
            "ip_address",
            "max_connections",
            "allowed_updates",
            "drop_pending_updates",
            "secret_token",
            "payload",
            "files",
        )
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_stop_message_live_location_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("chat_id", "message_id", "inline_message_id", "reply_markup", "payload", "result")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_stop_poll_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("chat_id", "message_id", "reply_markup", "payload", "result")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_unban_chat_member_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("chat_id", "user_id", "only_if_banned", "payload")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_unban_chat_sender_chat_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("chat_id", "sender_chat_id", "payload")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_unpin_all_chat_messages_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("chat_id", "payload")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_unpin_chat_message_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("chat_id", "message_id", "payload")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_upload_sticker_file_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("user_id", "png_sticker", "payload", "files", "result")
        return cls._get_async_mock_args(keys, async_mock_args)

    @classmethod
    def get_with_token_args(cls, async_mock_args) -> Dict[str, Any]:
        keys = ("kwds",)
        return cls._get_async_mock_args(keys, async_mock_args)
