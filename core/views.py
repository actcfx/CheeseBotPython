import nextcord
from nextcord import Embed
from nextcord.ui import View, Button
from core.classes import ErrorHandler


class Pagination_View(View):
    def __init__(self, _total_pages: int, _embeds: list[Embed]):
        super().__init__(timeout=None)
        self.current_page: int = 0
        self.total_pages: int = _total_pages
        self.embeds: list[Embed] = _embeds

        self.previous_button: Button = Button(label="<", style=nextcord.ButtonStyle.grey)
        self.next_button: Button = Button(label=">", style=nextcord.ButtonStyle.grey)

        self.previous_button.callback = self.previous_button_callback
        self.next_button.callback = self.next_button_callback

        if self.total_pages > 1:
            self.add_item(self.next_button)

    def update_buttons(self) -> None:
        self.clear_items()
        if self.current_page == 0:
            self.add_item(self.next_button)
        elif self.current_page == (self.total_pages - 1):
            self.add_item(self.previous_button)
        else:
            self.add_item(self.previous_button)
            self.add_item(self.next_button)

    async def previous_button_callback(self, interaction: nextcord.Interaction) -> None:
        try:
            if self.current_page > 0:
                self.current_page -= 1
                self.update_buttons()
                await interaction.response.edit_message(
                    embed=self.embeds[self.current_page], view=self
                )
        except Exception as unexpected_error:
            await ErrorHandler.handle_error(
                self,
                interaction,
                command="切換頁面",
                error_content=unexpected_error,
                error_type="unexpected_error",
            )

    async def next_button_callback(self, interaction: nextcord.Interaction) -> None:
        try:
            if self.current_page < self.total_pages:
                self.current_page += 1
                self.update_buttons()
                await interaction.response.edit_message(
                    embed=self.embeds[self.current_page], view=self
                )
        except Exception as unexpected_error:
            await ErrorHandler.handle_error(
                self,
                interaction,
                command="切換頁面",
                error_content=unexpected_error,
                error_type="unexpected_error",
            )
